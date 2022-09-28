#!/usr/bin/env python3
import argparse
import importlib.metadata
import logging
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any, List, Optional, TypedDict

import pyduktape
import requests
from pathvalidate import sanitize_filename, sanitize_filepath

__version__ = importlib.metadata.version("shutterfly_sites_api")


class Photo(TypedDict):
    id: str
    title: str
    url: str
    capture_date: Optional[datetime]


class Album(TypedDict):
    title: str
    photos: List[Photo]


def download_albums(albums: List[Album], download_dir: Path) -> bool:
    """Downloads all the given albums to the given directory."""
    if not download_dir.is_dir():
        logging.error(f"Does not exist or is not a directory: {download_dir}")
        return False

    for album in albums:
        logging.info(f"Downloading album: {album['title']}")
        group_path = download_dir / sanitize_filepath(album["title"])
        group_path.mkdir(exist_ok=True)
        for photo in album["photos"]:
            # Download file
            filename = group_path / sanitize_filename(photo["title"])
            if filename.exists():
                logging.info(f"> {filename} exists already, so skipping download")
                continue

            logging.info(f"> Downloading image: {filename}")
            req = requests.get(photo["url"], stream=True)
            with open(filename, "wb") as fd:
                for chunk in req.iter_content(chunk_size=65536):
                    fd.write(chunk)

            # Set file date to capture date
            if photo["capture_date"]:
                dt_str = photo["capture_date"].strftime("%Y%m%d%H%M")
                subprocess.run(["/usr/bin/touch", "-mt", dt_str, filename])

    return True


def _parse_js_data(js_text: str) -> Any:
    """Parses the Javascript data returned from Shutterfly."""
    context = pyduktape.DuktapeContext()
    context.eval_js(
        "var window = {}; var Shr = {}; var document = {}; document.write = function() {};"
    )
    context.eval_js(js_text)
    shr = context.get_global("Shr")
    if shr["P"]["kind"] == "ErrorPage":
        raise Exception("Not logged in, token invalid")

    return shr


def _get_albums_data(token: str, site: str) -> Any:
    """Fetches the raw albums data."""
    session = requests.Session()
    session.headers.update(
        {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0",
        }
    )
    session.cookies.update({"ShrAuth": token})
    resp = session.get(
        f"https://cmd.shutterfly.com/commands/format/js/?site={site}&page={site}%2fpictures&v=1&usejwt_token=true"
    )
    logging.debug(f"Response: {resp.text}")
    return _parse_js_data(resp.text)


def _parse_albums(albums_data: Any) -> List[Album]:
    """Parses the albums and photos data from the Shutterfly JS."""
    image_server = albums_data["AS"]["img"]

    ret: List[Album] = []
    groups = albums_data["P"]["sections"][0]["groups"]
    for group in groups:
        album: Album = {
            "title": group["title"],
            "photos": [],
        }

        for item in group["items"]:
            id = item["shutterflyId"]
            capture_date = (
                datetime.fromtimestamp(item["captureDate"]) if item["captureDate"] else None
            )
            photo: Photo = {
                "id": id,
                "title": item["title"],
                "url": f"https://{image_server}/v2/procgtaserv/{id}",
                "capture_date": capture_date,
            }
            album["photos"].append(photo)

        ret.append(album)

    return ret


def get_albums(token: str, site: str) -> List[Album]:
    """Gets the albums for all albums for the given site."""
    albums_data = _get_albums_data(token, site)
    return _parse_albums(albums_data)


def main() -> int:
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--token", type=str, required=True, help="Authentication token (ie ShrAuth cookie contents)"
    )
    parser.add_argument("--site", type=str, required=True, help="Share Sites site name")
    parser.add_argument(
        "--directory", type=str, default=".", help="Directory to download photos to"
    )
    parser.add_argument("--verbose", action="store_true", help="Turns on verbose logging")
    parser.add_argument("--version", action="version", version=__version__, help="Show version")

    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    albums = get_albums(args.token, args.site)
    success = download_albums(albums, Path(args.directory))
    return 0 if success else 1


if __name__ == "__main__":
    main()
