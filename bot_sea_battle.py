from api import Ship

X = 6
Y = 6
masiv_a = [["-"] * X for i in range(Y)]


def ship_enemy():
    ship = Ship()
    k = ship.ship_3(posiv="А1,А2,А3", masiv=masiv_a, player=2)
    k = ship.ship_2(posiv="Е1,Е2", masiv=k, player=2)
    k = ship.ship_2(posiv="Е5,Е6", masiv=k, player=2)
    k = ship.ship_1(posiv="Г4", masiv=k, player=2)
    k = ship.ship_1(posiv="А6", masiv=k, player=2)
    k = ship.ship_1(posiv="Г6", masiv=k, player=2)
    k = ship.ship_1(posiv="Г1", masiv=k, player=2)
    return k
