class TestExample:
    def test_one(self, class_timestamp):
        print(class_timestamp)
        assert 1 == 1

    def test_two(self, test_timestamp):
        print(test_timestamp)
        assert 2 == 2

    def test_three(self):
        assert 3 == 3