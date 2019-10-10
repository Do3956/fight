import random

from django.shortcuts import render
from lib.config import config
from django.views.decorators.http import require_POST, require_GET
from person.battle_way import BattleManager
from person import heros as module_heros

# Create your views here.


def have_a_battle(fighter_id_1, fighter_id_2, battle_way):
    """
    have_a_battle(1, 2, 'random_battle')
    """
    heros = config.heros
    battle_class = BattleManager.get_way(battle_way)
    if not battle_class:
        return f'error battle_way, try: {BattleManager.all_ways()}'
    if not (heros.get(fighter_id_1) and heros.get(fighter_id_2)):
        return 'error heros'

    fighter_list = map(lambda _id: getattr(
        module_heros, heros[_id]._class)(_id), [fighter_id_1, fighter_id_2])
    battle = battle_class(*fighter_list)
    winner = battle.battle()
    print(f"winner name is {winner.data.name}, hp:{winner.data.hp}")



