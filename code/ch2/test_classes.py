from cards import Card


class TestEquality:
    def test_equality(self):
        c1 = Card("something", "Brian", "todo", 123)
        c2 = Card("something", "Brian", "todo", 123)
        assert c1 == c2

    def test_inequality_with_diff_ids(self):
        c1 = Card("something", "Brian", "todo", 123)
        c2 = Card("something", "Brian", "todo", 4567)
        assert c1 == c2

    def test_inequality(self):
        c1 = Card("something", "Brian", "todo", 123)
        c2 = Card("completely different", "Okken", "done", 123)
        assert c1 != c2
