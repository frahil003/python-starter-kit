from __future__ import annotations


def hello(name: str | None = None) -> str:
    """Return a friendly greeting."""
    name = (name or "").strip()
    if not name:
        return "Hello!"
    return f"Hello, {name}!"


def excited(text: str, times: int = 3) -> str:
    """Add excitement to text, repeated a few times."""
    if times < 1:
        raise ValueError("times must be >= 1")
    return (text + "!") * times
