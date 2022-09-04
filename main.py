from api import NewGame
from api import Ship
from field import start_field
X = 6
Y = 6
ship = Ship()
masiv_a = [["-"] * X for i in range(Y)]
masiv_e = [["-"] * X for g in range(Y)]
amount = int(input("Сколько будет игроков, 1 или 2? "))
if amount == 1:
    name_player_1 = input('Как вас называть? ')
    new_game = NewGame(amount_player=amount, name_1=name_player_1, name_2=None)
    new_game.game_map_player_1()



ship_3 = input('Начнём с расстаноки, назовите координаты кораля состоящего из 3 палуб, через запятую (А1,Б1,В1)')
mapa = ship.ship_3(posiv=ship_3, masiv=masiv_a)
start_field(masiv_you=mapa, masiv_enemy=masiv_e)
ship_2 = input('Назовите координаты кораля состоящего из 2 палуб, через запятую (А1,Б1)')
mapa = ship.ship_2(posiv=ship_2, masiv=masiv_a)
start_field(masiv_you=mapa, masiv_enemy=masiv_e)
ship_2_1 = input('Назовите координаты кораля состоящего из 2 палуб, через запятую (А1,Б1)')
mapa = ship.ship_2(posiv=ship_2_1, masiv=mapa)
start_field(masiv_you=mapa, masiv_enemy=masiv_e)
ship_1_1 = input('Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)')
mapa = ship.ship_1(posiv=ship_1_1, masiv=mapa)
start_field(masiv_you=mapa, masiv_enemy=masiv_e)
ship_1_2 = input('Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)')
mapa = ship.ship_1(posiv=ship_1_2, masiv=mapa)
start_field(masiv_you=mapa, masiv_enemy=masiv_e)
ship_1_2 = input('Назовите координаты кораля состоящего из 1 палубы, через запятую (А1)')
mapa = ship.ship_1(posiv=ship_1_2, masiv=mapa)
start_field(masiv_you=mapa, masiv_enemy=masiv_e)







