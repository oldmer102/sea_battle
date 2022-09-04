from field import start_field

X = 6
Y = 6
my_slov = {}

slov_deat = {}
deat_position = []
busy_slot = []
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
    def slovar(self, name, coordinate):
        self.name = name
        self.coordinate = coordinate
        my_slov.update({name: coordinate})


    def ship_3(self, posiv, masiv):
        pos_b = 0
        pos_ch = 1
        pos_mas = 0
        mass = [["", ""], ["", ""], ["", ""]]
        name = posiv
        rules = PlacementRules()
        if len(posiv.split(",")) != 3:
            return False
        for k in posiv.split(","):
            for b in k:
                if b.isdigit() == False:
                    mass[pos_mas][pos_b] = ord(b.lower()) - 1072
                else:
                    mass[pos_mas][pos_ch] = int(b)-1
            pos_mas += 1
        if not rules.placement_check(position=mass):

            return False

        Ship.slovar(self, name, mass)
        jep = rules.placement_rules_x(position=my_slov, name=name)
        for i in jep:
            deat_position.append(i)
        slov_deat.update({name: jep})
        for i in busy_slot:
            for v in mass:
                if i == v:
                    return False
        for i in mass:
            busy_slot.append(i)
        for i in deat_position:
            for v in mass:
                if i == v:
                    print(i, v)
                    return False
        for k, n in mass:
            masiv[n][k] = "■"
        return masiv

    def ship_2(self, posiv, masiv):
        pos_b = 0
        pos_ch = 1
        pos_mas = 0
        mass = [["", ""], ["", ""]]
        name = posiv
        rules = PlacementRules()
        if len(posiv.split(",")) != 2:
            return False
        for k in posiv.split(","):
            for b in k:
                if b.isdigit() == False:
                    mass[pos_mas][pos_b] = ord(b.lower()) - 1072
                else:
                    mass[pos_mas][pos_ch] = int(b) - 1
            pos_mas += 1

        if not rules.placement_check(position=mass):
            return False
        Ship.slovar(self, name, mass)
        jep = rules.placement_rules_x(position=my_slov, name=name)
        for i in jep:
            deat_position.append(i)
        slov_deat.update({name: jep})
        for i in busy_slot:
            for v in mass:
                if i == v:
                    return False
        for i in mass:
            busy_slot.append(i)
        for i in deat_position:
            for v in mass:
                if i == v:
                    return False
        for k, n in mass:
            masiv[n][k] = "■"
        return masiv

    def ship_1(self, posiv, masiv):
        mass = [["", ""]]
        name = posiv
        rules = PlacementRules()
        if len(posiv.split(",")) != 1:
            return False
        for b in posiv:
            if b.isdigit() == False:
                mass[0][0] = ord(b.lower()) - 1072
            else:
                mass[0][1] = int(b) - 1
        Ship.slovar(self, name, mass)
        jep = rules.placement_rules_x(position=my_slov, name=name)
        for i in jep:
            deat_position.append(i)
        slov_deat.update({name: jep})
        for i in busy_slot:
            for v in mass:
                if i == v:
                    return False
        for i in mass:
            busy_slot.append(i)
        for i in deat_position:
            for v in mass:
                if i == v:
                    return False
        masiv[mass[0][1]][mass[0][0]] = "■"
        return masiv


class PlacementRules():
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
                    pass
                else:
                    return False
            elif position_1 == first:
                if position_2 + k == second or position_2 - k == second:
                    pass
                elif position_2 == second:
                    return False
            else:
                return False
            k += 1
        return True

    def placement_rules_x(self, position, name):
        self.name = name
        array = position[self.name]
        print(array)
        zapret = []
        position_1 = array[0][0]
        position_2 = array[0][1]
        position_last_1 = array[-1][0]
        position_last_2 = array[-1][1]
        # Вертикаль
        if len(array) > 1:
            if array[1][0] == position_1:
                for k, v in array[1:]:
                    zapret.append([k - 1, v + 1])
                    zapret.append([k - 1, v - 1])
                    zapret.append([k + 1, v + 1])
                    zapret.append([k + 1, v - 1])
                    zapret.append([position_1 - 1, position_2 - 1])
                    zapret.append([position_1, position_2 - 1])
                    zapret.append([position_1 + 1, position_2 - 1])
                    zapret.append([position_last_1, position_last_2 + 1])
            # Горизонталь
            if array[1][1] == position_2:
                for k, v in array[1:]:
                    zapret.append([k, v - 1])
                    zapret.append([k, v + 1])
                    zapret.append([position_1, position_2 - 1])
                    zapret.append([position_1, position_2 + 1])
                    zapret.append([position_1 - 1, position_2 - 1])
                    zapret.append([position_1 - 1, position_2 + 1])
                    zapret.append([position_1 - 1, position_2])
                    zapret.append([position_last_1 + 1, position_last_2 + 1])
                    zapret.append([position_last_1 + 1, position_last_2 - 1])
                    zapret.append([position_last_1 + 1, position_last_2])
        if len(array) == 1:
            zapret.append([position_1, position_2 - 1])
            zapret.append([position_1, position_2 + 1])
            zapret.append([position_1 - 1, position_2 + 1])
            zapret.append([position_1 - 1, position_2 - 1])
            zapret.append([position_1 - 1, position_2])
            zapret.append([position_1 + 1, position_2 + 1])
            zapret.append([position_1 + 1, position_2 - 1])
            zapret.append([position_1 + 1, position_2])
        return zapret


class StartGame():
    def shot(self, shot_position, array):
        mass = [["", ""]]
        if len(shot_position.split(",")) != 1:
            return False
        for b in shot_position:
            if b.isdigit() == False:
                mass[0][0] = ord(b.lower()) - 1072
            else:
                mass[0][1] = int(b) - 1
        array[mass[0][1]][mass[0][0]] = 'X'
        return array

    def shot_ship(self,shot_position):
        mass = [["", ""]]
        if len(shot_position.split(",")) != 1:
            return False
        for b in shot_position:
            if b.isdigit() == False:
                mass[0][0] = ord(b.lower()) - 1072
            else:
                mass[0][1] = int(b) - 1

        for k, v in my_slov.items():
            for i in v:
                for b in mass:
                    if i == b:
                        my_slov.remove(i)


    def deat_ship(self, array):
        for k, v in my_slov.items():
            if len(v) == 0:
                del my_slov[k]
                deat = slov_deat[k]
                for i, m in deat:
                    array[i][m] = 'X'

                del slov_deat[k]
                return deat
            else:
                return False



