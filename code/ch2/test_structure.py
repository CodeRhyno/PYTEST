from cards import Card


def test_to_dict():
    # GIVEN / ARRANGE
    c1 = Card("something", "Brian", "todo", 123)

    # WHEN / ACT
    c2 = c1.to_dict()

    # THEN /ASSERT
    c2_expected = {
        "summary": "something",
        "owner": "Brian",
        "state": "todo",
        "id": 123
    }
    assert c2 == c2_expected
