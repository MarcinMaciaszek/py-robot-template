from robot.api.deco import library, keyword  # type: ignore


@library()
class TestLibrary:
    """A simple test library example."""

    @keyword("Add Two Integers")
    def add_two_ints(self, a: int, b: int) -> int:
        """Returns the sum of two integers."""
        assert isinstance(a, int), (
            f"You should provide int value not {type(a)} for a parameter!!!"
        )
        assert isinstance(b, int), (
            f"You should provide int value not {type(b)} for b parameter!!!"
        )
        return a + b
