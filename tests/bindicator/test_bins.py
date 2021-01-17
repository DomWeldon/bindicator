import datetime


def test__query_next_date_for_each_bin():
    # arrange
    from bindicator import bins

    # act
    next_dates = bins._query_next_date_for_each_bin()

    # assert
    assert len(next_dates) == 4


def test__get_next_bin_day():
    # arrange
    from bindicator import bins
    from bindicator.config import config

    today = datetime.date.today()

    # act
    next_bin_day = bins._get_next_bin_day()

    # assert
    assert next_bin_day >= today
    assert next_bin_day.strftime("%A") == config.BIN_DAY
