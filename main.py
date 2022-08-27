from api import NewGame

player_1 = str(input('Имя первого игрока: '))
player_2 = str(input('Имя второго игрока: '))

start = NewGame(amount_player=1, name_1=player_1, name_2=player_2)

start.game_map_player_1()







