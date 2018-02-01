import pytest

from .create_world import World


@pytest.fixture(scope="module")
def world():
    return World()


def test_get_world(world):
    assert world.physics
    assert world.biology
