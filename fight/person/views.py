import random

from django.shortcuts import render
from lib.config import config
from django.views.decorators.http import require_POST, require_GET
from person.battle_way import battleWays
from person.heros import allHeros

# Create your views here.


def have_a_battle(fighter_id_1, fighter_id_2, battle_way):
    """
    have_a_battle(1, 2, 'random_battle')
    """
    battle_meth = battleWays.get_way(battle_way)
    if not battle_meth:
        return 'error battle_way'
    if not (config.heros.get(fighter_id_1) and config.heros.get(fighter_id_2)):
        return

    heros = list(map(lambda x: allHeros.get_hero(x), (fighter_id_1, fighter_id_2)))
    battle = battle_meth(heros)
    winner = battle.battle()
    print(f"winner name is {winner.data.name}, hp:{winner.data.hp}")

