from Python_test.main import calendar_yield



def test_response_time_calendar():
    assert calendar_yield.response_time(calendar_yield.range_days)


def test_calendar():
    assert calendar_yield.range_days


def test_show_dates():
    assert calendar_yield.show_dates


def test_twins_prime():
    assert calendar_yield.twins_prime


def test_response_time_twins_prime():
    assert calendar_yield.response_time(calendar_yield.twins_prime)
