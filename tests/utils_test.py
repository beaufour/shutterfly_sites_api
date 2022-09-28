from shutterfly_sites_api.utils import lat_long_decimal_to_dms


def test_lat_long_decimal_to_dms() -> None:
    assert lat_long_decimal_to_dms("+40.446,-79.982") == ((40, 26, 45), (-79, 58, 55))
