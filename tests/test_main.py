from backpackiest.main import greet


def test_greet() -> None:
    assert greet("world") == "Hello, world!"


def test_greet_empty() -> None:
    assert greet("") == "Hello, !"
