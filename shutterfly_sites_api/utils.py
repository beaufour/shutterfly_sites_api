from typing import Tuple

DMS = Tuple[int, int, int]
Coordinate = Tuple[DMS, DMS]


def decimal_to_dms(decimal: float) -> DMS:
    """Converts a geo coordinate decimal to (degrees, minutes, seconds)"""
    negative = decimal < 0
    decimal = abs(decimal)
    minutes, seconds = divmod(decimal * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    if negative:
        if degrees > 0:
            degrees = -degrees
        elif minutes > 0:
            minutes = -minutes
        else:
            seconds = -seconds
    return (int(degrees), int(minutes), int(seconds))


def lat_long_decimal_to_dms(coord: str) -> Coordinate:
    """Converts geo lat long coordinates from decimals to degrees, minutes,
    seconds.

    See: https://en.wikipedia.org/wiki/Geographic_coordinate_conversion
    """
    (N, W) = coord.split(",")
    return (decimal_to_dms(float(N)), decimal_to_dms(float(W)))
