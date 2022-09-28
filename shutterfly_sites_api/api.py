#!/usr/bin/env python3
import argparse
import importlib.metadata
import logging
import subprocess
from datetime import datetime
from pathlib import Path

import pyduktape
import requests
from pathvalidate import sanitize_filename, sanitize_filepath

__version__ = importlib.metadata.version("shutterfly_sites_api")


def get_photos(token: str, site: str, download_dir: Path) -> bool:
    if not download_dir.is_dir():
        logging.error(f"Does not exist or is not a directory: {download_dir}")
        return False

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
    js_text = resp.text
    logging.debug(f"Response: {js_text}")

    context = pyduktape.DuktapeContext()
    context.eval_js(
        "var window = {}; var Shr = {}; var document = {}; document.write = function() {};"
    )
    context.eval_js(js_text)
    shr = context.get_global("Shr")
    if shr["P"]["kind"] == "ErrorPage":
        logging.error("Not logged in, token invalid")
        return False

    image_server = shr["AS"]["img"]

    groups = shr["P"]["sections"][0]["groups"]
    for group in groups:
        group_title = group["title"]
        logging.info(f"Downloading album: {group_title}")
        group_path = download_dir / sanitize_filepath(group_title)
        group_path.mkdir(exist_ok=True)
        for image in group["items"]:
            id = image["shutterflyId"]
            title = image["title"]
            captureDate = image["captureDate"]
            url = f"https://{image_server}/v2/procgtaserv/{id}"

            # Download file
            filename = group_path / sanitize_filename(title)
            if filename.exists():
                logging.info(f"> {filename} exists already, so skipping download")
                continue

            logging.info(f"> Downloading image: {filename}")
            req = requests.get(url, stream=True)
            with open(filename, "wb") as fd:
                for chunk in req.iter_content(chunk_size=65536):
                    fd.write(chunk)

            # Set file date
            if captureDate:
                dt = datetime.fromtimestamp(captureDate)
                dt_str = f"{dt.year}{dt.month:02d}{dt.day:02d}{dt.hour:02d}{dt.minute:02d}"
                subprocess.run(["/usr/bin/touch", "-mt", dt_str, filename])

    return True


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

    success = get_photos(args.token, args.site, Path(args.directory))
    return 0 if success else 1


if __name__ == "__main__":
    main()
