import pytest

from healerino.npc import NPC


@pytest.fixture
def npc():
    return NPC(name="NPC", hp=1, ap=1)


def test_npc_attributes(npc):
    assert npc.name == "NPC"
    assert npc.hp == 1
    assert npc.ap == 1


def test_npc_is_alive(npc):
    assert not npc.is_dead

def test_npc_is_dead(npc):
    npc.hp = 0
    assert npc.is_dead


def test_npc_attack(npc):
    target = NPC(name="Noob", hp=2, ap=1)
    npc.attack(target)
    assert target.hp == 1
    npc.attack(target)
    assert target.is_dead
    assert target.hp == 0


def test_npc_attack_overkill(npc):
    strong_npc = NPC(name="Strong NPC", hp=100, ap=100)
    strong_npc.attack(npc)
    assert npc.hp == 0
    assert npc.is_dead
