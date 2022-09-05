from field import start_field
#Размер поля
X = 6
Y = 6
#словарь расстановки
my_slov = {}
my_slov_enemy = {'А1,Б1,В1': [[0, 0], [1, 0], [2, 0]], 'Е1,Е2': [[5, 0], [5, 1]], 'Е4,Е5': [[5, 3], [5, 4]], 'А3': [[0, 2]], 'Б5': [[1, 4]], 'Г3': [[3, 2]]}
#словарь содержит координаты взрыва корабля
slov_deat = {}
slov_deat_enemy = {}
#промежуточный список
deat_position = []
deat_position_enemy = []
# проверка на занятость позиции
busy_slot = []
busy_slot__enemy = []
masiv_a = [["-"] * X for i in range(Y)]


class NewGame(object):
    #Наименование игрок
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
    #Запись в словарь расположения кораблей
    def slovar(self, name, coordinate):
        self.name = name
        self.coordinate = coordinate
        my_slov.update({name: coordinate})

    def slovar_enemy(self, name, coordinate):
        self.name = name
        self.coordinate = coordinate
        my_slov_enemy.update({name: coordinate})

#Расстановка 3 коралей
    def ship_3(self, posiv, masiv, player):
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
        if player == 1:
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
        if player == 2:
            Ship.slovar_enemy(self, name, mass)
            jep = rules.placement_rules_x(position=my_slov_enemy, name=name)
            for i in jep:
                deat_position_enemy.append(i)
            slov_deat_enemy.update({name: jep})
            for i in busy_slot__enemy:
                for v in mass:
                    if i == v:
                        return False
            for i in mass:
                busy_slot__enemy.append(i)
            for i in deat_position_enemy:
                for v in mass:
                    if i == v:
                        return False
            for k, n in mass:
                masiv[n][k] = "-"
            return masiv



    # Расстановка 2 коралей
    def ship_2(self, posiv, masiv, player):
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
        if player == 1:
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
        if player == 2:
            Ship.slovar_enemy(self, name, mass)
            jep = rules.placement_rules_x(position=my_slov_enemy, name=name)
            for i in jep:
                deat_position_enemy.append(i)
            slov_deat_enemy.update({name: jep})
            for i in busy_slot__enemy:
                for v in mass:
                    if i == v:
                        return False
            for i in mass:
                busy_slot__enemy.append(i)
            for i in deat_position_enemy:
                for v in mass:
                    if i == v:
                        return False
            for k, n in mass:
                masiv[n][k] = "-"
            return masiv

    # Расстановка 1 коралей
    def ship_1(self, posiv, masiv, player):
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
        if player == 1:
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
        if player == 2:
            Ship.slovar_enemy(self, name, mass)
            jep = rules.placement_rules_x(position=my_slov_enemy, name=name)
            for i in jep:
                deat_position_enemy.append(i)
            slov_deat_enemy.update({name: jep})
            for i in busy_slot__enemy:
                for v in mass:
                    if i == v:
                        return False
            for i in mass:
                busy_slot__enemy.append(i)
            for i in deat_position_enemy:
                for v in mass:
                    if i == v:
                        return False
            for k, n in mass:
                masiv[n][k] = "-"
            return masiv


class PlacementRules():
    #проверка на горизонталь вертикаль и что бы соответствовал длине
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
#Запись взрыва кораля
    def placement_rules_x(self, position, name):
        self.name = name
        array = position[self.name]
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
    #запись выстрела
    def shot_you(self, shot_position, array):
        mass = [["", ""]]
        if len(shot_position.split(",")) != 1:
            return False
        for b in shot_position:
            if b.isdigit() == False:
                mass[0][0] = ord(b.lower()) - 1072
            else:
                mass[0][1] = int(b) - 1
        array[mass[0][1]][mass[0][0]] = 'X'
        for k, v in my_slov_enemy.items():
            for i in v:
                for b in mass:
                    if i == b:
                        my_slov_enemy[k].remove(i)
        for k, v in my_slov_enemy.items():
            if len(v) == 0:

                del my_slov_enemy[k]
                deat = slov_deat_enemy[k]
                for i, m in deat:
                    if i >= 0 and m >= 0:
                        array[m][i] = 'X'
                del slov_deat_enemy[k]
                return array

        return array

#Закраска полей вокруг корабля
    # def deat_ship(self, array):
    #     for k, v in my_slov.items():
    #         if len(v) == 0:
    #
    #             del my_slov[k]
    #             deat = slov_deat[k]
    #             for i, m in deat:
    #                 if i >= 0 and m >= 0:
    #                     array[m][i] = 'X'
    #             del slov_deat[k]
    #             return array
    #         else:
    #             return False



