import pathlib
from datetime import datetime
from typing import List

import pytest
from shutterfly_sites_api.api import Album, _parse_albums, _parse_js_data

FIXTURE_DIR = pathlib.Path(__file__).parent.resolve() / "fixtures"


def load_fixture(path: str) -> str:
    f = open(FIXTURE_DIR / path, "r")
    return f.read()


def test_parse_js_data() -> None:
    with pytest.raises(Exception):
        _parse_js_data(load_fixture("error_page.js"))


def test_get_albums() -> None:
    albums_data = _parse_js_data(load_fixture("fixture_1.js"))
    albums = _parse_albums(albums_data)
    albums_correct: List[Album] = [
        {
            "title": "Album Title 1",
            "photos": [
                {
                    "id": "423423",
                    "title": "IMG_2275.JPG",
                    "url": "https://uniim-share.shutterfly.com/v2/procgtaserv/423423",
                    "capture_date": datetime(2022, 9, 27, 4, 39, 34),
                },
                {
                    "id": "67547",
                    "title": "IMG_2277.JPG",
                    "url": "https://uniim-share.shutterfly.com/v2/procgtaserv/67547",
                    "capture_date": datetime(2022, 9, 27, 4, 44, 13),
                },
                {
                    "id": "234241",
                    "title": "IMG_2279.JPG",
                    "url": "https://uniim-share.shutterfly.com/v2/procgtaserv/234241",
                    "capture_date": datetime(2022, 9, 27, 4, 44, 33),
                },
            ],
        },
        {
            "title": "Album Title 2",
            "photos": [
                {
                    "id": "235525525",
                    "title": "IMG_1849.JPG",
                    "url": "https://uniim-share.shutterfly.com/v2/procgtaserv/235525525",
                    "capture_date": datetime(2022, 9, 23, 6, 38, 38),
                },
            ],
        },
    ]
    assert albums == albums_correct
