from api import NewGame
from api import Ship
from api import StartGame
from field import start_field
from api import finish, finish_enemy

from bot_sea_battle import ship_enemy
import random


shot_mot = []
X = 6
Y = 6
ship = Ship()
game = StartGame()
masiv_a = [["-"] * X for i in range(Y)]
masiv_e = [["-"] * X for g in range(Y)]

name_player_1 = input("Как вас называть? ")
new_game = NewGame(amount_player=1, name_1=name_player_1, name_2=None)
new_game.game_map_player_1()

tru = False
k = True

while len(finish) < 10 or len(finish_enemy) < 10:
    while not tru:
        ship_3 = input(
            "Начнём с расстаноки, назовите координаты кораля состоящего из 3 палуб, через запятую (А1,Б1,В1)"
        )
        mapa = ship.ship_3(posiv=ship_3, masiv=masiv_a, player=1)
        if not mapa:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while not tru:
        ship_2 = input(
            "Назовите координаты кораля состоящего из 2 палуб, через запятую (А1,Б1)"
        )
        mapa = ship.ship_2(posiv=ship_2, masiv=masiv_a, player=1)
        if not mapa:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while not tru:
        ship_2_1 = input(
            "Назовите координаты кораля состоящего из 2 палуб, через запятую (А1,Б1)"
        )
        mapa = ship.ship_2(posiv=ship_2_1, masiv=masiv_a, player=1)
        if not mapa:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while not tru:
        ship_1_1 = input(
            "Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)"
        )
        mapa = ship.ship_1(posiv=ship_1_1, masiv=masiv_a, player=1)
        if not mapa:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while not tru:
        ship_1_2 = input(
            "Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)"
        )
        mapa = ship.ship_1(posiv=ship_1_2, masiv=masiv_a, player=1)
        if not mapa:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while not tru:
        ship_1_3 = input(
            "Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)"
        )
        mapa = ship.ship_1(posiv=ship_1_3, masiv=masiv_a, player=1)
        if not mapa:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while not tru:
        ship_1_4 = input(
            "Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)"
        )
        mapa = ship.ship_1(posiv=ship_1_4, masiv=masiv_a, player=1)
        if not mapa:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)

    ship_enemy()

    while len(finish) < 10 or len(finish_enemy) < 10:

        cen = False
        while not cen:
            shot = input("Выстрел!")
            masiv_F = game.shot_you(shot_position=shot, array=masiv_e)
            if masiv_F:
                cen = masiv_F
        cen = False
        while not cen:
            shot_ene = [random.randrange(0, 5), random.randrange(0, 5)]
            masiv_G = game.shot_eneny(shot_position=[shot_ene], array=mapa)
            if masiv_G:
                cen = masiv_G
        start_field(masiv_you=cen, masiv_enemy=masiv_F)
        if len(finish) == 11 or len(finish_enemy) == 11:
            break
    if len(finish) == 11 or len(finish_enemy) == 11:
        break


if len(finish) == 11:
    print("Вы победили!")
elif len(finish_enemy) == 11:
    print("Победил бот!")
