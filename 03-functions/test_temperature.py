from temperature import celsius_to_fahrenheit, describe, fahrenheit_to_celsius


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32
    assert fahrenheit_to_celsius(32) == 0


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212


def test_round_trip():
    for c in (-40, -3.5, 0, 21.7, 100):
        back = fahrenheit_to_celsius(celsius_to_fahrenheit(c))
        assert abs(back - c) < 1e-9


def test_describe():
    assert describe(-5) == "freezing"
    assert describe(10) == "cold"
    assert describe(20) == "mild"
    assert describe(30) == "hot"
