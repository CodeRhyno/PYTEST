from cards import Card


def test_equality_fail():
    c1 = Card("sit there", "Brian")
    c2 = Card("do something", "Okken")
    assert c1 == c2
