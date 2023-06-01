from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("trybe", 10) == "ebyrt"
    assert encrypt_message("trybe", 3) == "yrt_eb"
    assert encrypt_message("trybe", 2) == "eby_rt"

    with pytest.raises(TypeError):
        encrypt_message("trybe", "str")
