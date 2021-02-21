import datetime
import enum
import typing

import lxml.html
import requests

from .config import config

TODAY = datetime.date.today()


class Bins(enum.Enum):
    """Bin colours as decided over a beer in the kitchen"""

    # for paper
    BLUE: typing.Tuple[int, int, int] = (10, 0, 255)
    # garden waste and food
    GREEN: typing.Tuple[int, int, int] = (0, 255, 0)
    # bottles and cans, lovely lovely cans
    BROWN: typing.Tuple[int, int, int] = (255, 22, 0)
    # non-recyclable waste, using white as black not possible when on
    BLACK: typing.Tuple[int, int, int] = (255, 0, 255)


def _query_next_date_for_each_bin(
    url=config.COUNCIL_URL,
) -> typing.Dict[Bins, datetime.date]:
    """Query the council website to get the next collection dates."""
    # query the council website
    r = requests.get(url)
    tree = lxml.html.fromstring(r.text)

    # process with xpaths
    return {
        getattr(Bins, k.upper()): datetime.datetime.strptime(
            tree.xpath(
                f"//div[contains(@class, 'service-item-{k}')]"
                "/div/p[not(contains(@class, 'sub-title'))]/text()"
            )[0].strip(),
            "%A, %d %B %Y",
        ).date()
        for k in {"black", "blue", "green", "brown"}
    }


def _get_next_bin_day(today=TODAY, bin_day=config.BIN_DAY) -> datetime.date:
    """Get the date of the next bin day."""
    day = today
    i = 0
    while day.strftime("%A") != bin_day and i < 7:
        i += 1
        day += datetime.timedelta(days=1)

    if i >= 7:
        raise ValueError("Next bin day not found.")

    return day


NEXT_BIN_DAY = _get_next_bin_day()
print("next bin day", NEXT_BIN_DAY)
NEXT_COLLECTION_DATES = _query_next_date_for_each_bin()
print("next collections", NEXT_COLLECTION_DATES)
COLLECTIONS_THIS_WEEK = {
    k for k, v in NEXT_COLLECTION_DATES.items() if v == NEXT_BIN_DAY
}
print("collections this week", COLLECTIONS_THIS_WEEK)

# this is messy - I think there may also be a third option of three bins?
NEXT_BINS = (
    (COLLECTIONS_THIS_WEEK.pop(), COLLECTIONS_THIS_WEEK.pop())
    if len(COLLECTIONS_THIS_WEEK) > 1
    else ((b := COLLECTIONS_THIS_WEEK.pop()), b)
)

# NEXT_BINS = (Bins.BLACK, Bins.GREEN)
