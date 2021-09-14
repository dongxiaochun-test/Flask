
class TestClass:
    def test_one(self):
        x="123"
        assert "1" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b
