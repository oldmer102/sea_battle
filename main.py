from api import NewGame
from api import Ship
from field import start_field
# player_1 = str(input('Имя первого игрока: '))
# player_2 = str(input('Имя второго игрока: '))
# masiv_a = [['-'] * X for i in range(Y)]
# start = NewGame(amount_player=1, name_1=player_1, name_2=player_2)
ship = Ship()
#
#
# start.game_map_player_1()

#ship_rasp = str(input('Начнём с расстановки кораблей, в игре есть 3 вида: 1 палубных (4шт), 2 палубных (2шт), 3 палубный (1шт). Для расстановки используйте две координаты с перечисление через заяпятую(А1,Б1,В1): '))
#ship.ship(ship_posiv=ship_rasp)
X = 6
Y = 6
a = 'А1,Б1,В1'
b = 'А2,Б2'
c = 'А3'
masiv_a = [['-'] * X for i in range(Y)]
masiv_e = [['-'] * X for i in range(Y)]
k = ship.ship_3(posiv=a,masiv=masiv_a)
k = ship.ship_2(posiv=b,masiv=k)
k = ship.ship_1(posiv=c,masiv=k)
start_field(k,masiv_e)






