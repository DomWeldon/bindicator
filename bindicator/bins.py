import datetime
import enum
import typing


class Bins(enum.Enum):
    """Bin colours as decided over a beer in the kitchen"""
    # for paper
    BLUE: typing.Tuple[int, int, int] = (99, 34, 147)
    # garden waste and food
    GREEN: typing.Tuple[int, int, int] = (0, 255, 0)
    # bottles and cans, lovely lovely cans
    BROWN: typing.Tuple[int, int, int] = (255, 56, 0)
    # non-recyclable waste, using white as black not possible when on
    BLACK: typing.Tuple[int, int, int] = (255, 255, 255)


# hardcoding for tonight
BIN_SCHEDULE = {
    datetime.date(2021, 1, 18): (Bins.BLACK, Bins.GREEN,),
    datetime.date(2021, 1, 18): (Bins.BLUE, Bins.BROWN,),
}

# TODO: write a proper connector to the council API
NEXT_BINS = (Bins.BLACK, Bins.GREEN,)
# If you're reading this (NERD), it's because I want it to work for the night
# before bin day, which is tomorrow.
