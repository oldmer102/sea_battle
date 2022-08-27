from field import start_field


class NewGame(object):
    def __init__(self, amount_player, name_1, name_2):
        self.player_1 = name_1
        self.amount = amount_player
        if amount_player == 2:
            self.player_2 = name_2
        if amount_player == 1:
            self.player_2 = 'БотВасилий'

    def game_map_player_1(self):
        game_map_player_1 = self.player_1 + '\n'
        print(game_map_player_1)
        start_field()

    def game_map_player_2(self, open_field):
        game_map_player_2 = self.player_2 + '\n' + open_field
        return game_map_player_2




