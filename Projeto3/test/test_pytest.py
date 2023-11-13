from ..src.main import Password

def test_password():
    assert Password.verify(password_to_test=Password.get_entry())