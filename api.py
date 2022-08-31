from field import start_field

X = 6
Y = 6

masiv_a = [["-"] * X for i in range(Y)]


class NewGame(object):
    def __init__(self, amount_player, name_1, name_2):
        self.player_1 = name_1
        self.amount = amount_player
        if amount_player == 2:
            self.player_2 = name_2
        if amount_player == 1:
            self.player_2 = "БотВасилий"

    def game_map_player_1(self):
        print(self.player_1 + "\n")
        game_map_player_1 = start_field(masiv_a, masiv_a)
        return game_map_player_1

    def game_map_player_2(self):
        print(self.player_2 + "\n")
        game_map_player_2 = start_field(masiv_a, masiv_a)
        return game_map_player_2


class Ship(object):
    def ship_3(self, posiv, masiv):
        pos_b = 0
        pos_ch = 1
        pos_mas = 0
        mass = [["", ""], ["", ""], ["", ""]]
        for k in posiv.split(","):
            for b in k:
                if b.isdigit() == False:
                    mass[pos_mas][pos_b] = ord(b.lower()) - 1071
                else:
                    mass[pos_mas][pos_ch] = int(b)
            pos_mas += 1
        for k, n in mass:
            masiv[n - 1][k - 1] = "■"
        return masiv

    def ship_2(self, posiv, masiv):
        pos_b = 0
        pos_ch = 1
        pos_mas = 0
        mass = [["", ""], ["", ""]]
        for k in posiv.split(","):
            for b in k:
                if b.isdigit() == False:
                    mass[pos_mas][pos_b] = ord(b.lower()) - 1071
                else:
                    mass[pos_mas][pos_ch] = int(b)
            pos_mas += 1
        for k, n in mass:
            masiv[n - 1][k - 1] = "■"
        return masiv

    def ship_1(self, posiv, masiv):
        mass = ["", ""]
        for b in posiv:
            if b.isdigit() == False:
                mass[0] = ord(b.lower()) - 1071
            else:
                mass[1] = int(b)
        masiv[mass[1] - 1][mass[0] - 1] = "■"
        return masiv


class PlacementRules(object):
    def placement_check(self, position):
        position_1 = position[0][0]
        position_2 = position[0][1]
        amount = len(position)
        k = 1
        if amount == 1:
            return True
        if amount > 3:
            return False
        for first, second in position[1:]:
            if position_1 != first and (
                position_1 + k == first or position_1 - k == first
            ):
                if position_2 == second:
                    return True
                else:
                    return False
            elif position_1 == first:
                if position_2 + k == second or position_2 - k == second:
                    return True
                elif position_2 == second:
                    return False
            else:
                return False
            k += 1
