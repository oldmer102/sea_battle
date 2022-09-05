from api import NewGame
from api import Ship
from api import StartGame
from field import start_field
from api import finish
from api import my_slov
from bot_sea_battle import ship_enemy
import random


shot_mot = []
X = 6
Y = 6
ship = Ship()
game = StartGame()
masiv_a = [["-"] * X for i in range(Y)]
masiv_e = [["-"] * X for g in range(Y)]
amount = int(input("Сколько будет игроков, 1 или 2? "))
if amount == 1:
    name_player_1 = input('Как вас называть? ')
    new_game = NewGame(amount_player=amount, name_1=name_player_1, name_2=None)
    new_game.game_map_player_1()
tru = False
k = 0
while k < 10:
    while tru == False:
        ship_3 = input(
            'Начнём с расстаноки, назовите координаты кораля состоящего из 3 палуб, через запятую (А1,Б1,В1)')
        mapa = ship.ship_3(posiv=ship_3, masiv=masiv_a, player=1)
        if mapa == False:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while tru == False:
        ship_2 = input('Назовите координаты кораля состоящего из 2 палуб, через запятую (А1,Б1)')
        mapa = ship.ship_2(posiv=ship_2, masiv=masiv_a, player=1)
        if mapa == False:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while tru == False:
        ship_2_1 = input('Назовите координаты кораля состоящего из 2 палуб, через запятую (А1,Б1)')
        mapa = ship.ship_2(posiv=ship_2_1, masiv=mapa, player=1)
        if mapa == False:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while tru == False:
        ship_1_1 = input('Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)')
        mapa = ship.ship_1(posiv=ship_1_1, masiv=mapa, player=1)
        if mapa == False:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while tru == False:
        ship_1_2 = input('Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)')
        mapa = ship.ship_1(posiv=ship_1_2, masiv=mapa, player=1)
        if mapa == False:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    tru = False
    while tru == False:
        ship_1_3 = input('Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)')
        mapa = ship.ship_1(posiv=ship_1_3, masiv=mapa, player=1)
        if mapa == False:
            tru = False
        else:
            tru = True
            start_field(masiv_you=mapa, masiv_enemy=masiv_e)
    ship_enemy()
    while len(finish) < 10:
        shot = input('Выстрел!')
        masiv_e = game.shot_you(shot_position=shot, array=masiv_e)
        shot_ene = [random.randrange(0, 5), random.randrange(0, 5)]
        mapa = game.shot_eneny(shot_position=[shot_ene], array=mapa)

        start_field(masiv_you=mapa, masiv_enemy=masiv_e)










