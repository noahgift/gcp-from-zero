from app import marco


def test_marco():
    assert marco("Marco") == "Marco"
    assert marco("Peter") == "Bob"
