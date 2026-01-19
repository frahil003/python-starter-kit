import pytest

from my_project.greetings import excited, hello


def test_hello_default() -> None:
    assert hello() == "Hello!"


def test_hello_name() -> None:
    assert hello("Frank") == "Hello, Frank!"


def test_excited_repeats() -> None:
    assert excited("Yay", times=2) == "Yay!Yay!"


def test_excited_rejects_invalid_times() -> None:
    with pytest.raises(ValueError):
        excited("Nope", times=0)
