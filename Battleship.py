Map_Battleship_Player_One = []


class MapBattleship:
    def __init__(self, map_size):
        self.map_size = map_size

    def create_map(self):
        map_element = "*"
        for x in range(self.map_size):
            map_line = []
            for y in range(self.map_size):
                map_line += map_element
            Map_Battleship_Player_One.append(map_line)

    def print_map(self):
        for x in range(self.map_size):
            print(Map_Battleship_Player_One[x])


class Ships:
    # Types: pb, b, s, c
    # Start: location on board, needs to be array, Between 0 and 9
    # Orientation: Up, Down, Left, Right
    def __init__(self, ship_type, start_one, start_two, orientation):
        self.ship_type = ship_type
        self.start_one = start_one
        self.start_two = start_two
        self.orientation = orientation

    def get_length(self):
        if self.ship_type == "P":
            return 2
        if self.ship_type == "B":
            return 3
        if self.ship_type == "S":
            return 3
        if self.ship_type == "D":
            return 4
        if self.ship_type == "C":
            return 5

    def check_map(self):
        can_place = False
        if self.orientation == "Up":
            if self.start_one - self.get_length() < 0:
                print("Error")
            else:
                can_place = True

        if self.orientation == "Down":
            if self.start_one + self.get_length() > 9:
                print("Error")
            else:
                can_place = True

        if self.orientation == "Left":
            if self.start_two - self.get_length() < 0:
                print("Error")
            else:
                can_place = True

        if self.orientation == "Right":
            if self.start_two + self.get_length() > 9:
                print("Error")
            else:
                can_place = True

        if can_place:
            return True
        else:
            return False

    def put_in_map(self):
        ship_type = str(self.ship_type)
        if self.check_map():
            for x in range(self.get_length()):
                if self.orientation == "Up":
                    Map_Battleship_Player_One[self.start_one - x][self.start_two] = ship_type
                if self.orientation == "Down":
                    Map_Battleship_Player_One[self.start_one + x][self.start_two] = ship_type
                if self.orientation == "Left":
                    Map_Battleship_Player_One[self.start_one][self.start_two - x] = ship_type
                if self.orientation == "Right":
                    Map_Battleship_Player_One[self.start_one][self.start_two + x] = ship_type
        else:
            print("Enter Again ship " + ship_type + " in orientation " + self.orientation)


class player_input:
    def __init__(self):
        self.x_val = 0
        self.y_val = 0

    def input_values(self, x_value, y_value):
        self.x_val = x_value
        self.y_val = y_value

    def check_attmpt(self):
        if Map_Battleship_Player_One[self.x_val][self.y_val] == "*" or Map_Battleship_Player_One[self.x_val][
            self.y_val] == "~":
            print("Missed")
        elif Map_Battleship_Player_One[self.x_val][self.y_val] != "*" or Map_Battleship_Player_One[self.x_val][
            self.y_val] != "~":
            print("Player Hit")
            Map_Battleship_Player_One[self.x_val][self.y_val] = "~"
            print("Player Gets another turn")


def check_map_status():
    is_dead = True
    for x in range(10):
        for y in range(10):
            if Map_Battleship_Player_One[x][y] != "*" and Map_Battleship_Player_One[x][y] != "~":
                is_dead = False

    return is_dead


def main():
    map_battle = MapBattleship(10)
    map_battle.create_map()
    player_one_input = player_input()

    ship1 = Ships("P", 0, 0, "Right")
    ship1.check_map()
    ship1.put_in_map()

    ship2 = Ships("P", 8, 1, "Right")
    ship2.check_map()
    ship2.put_in_map()

    ship3 = Ships("B", 1, 6, "Left")
    ship3.check_map()
    ship3.put_in_map()

    ship4 = Ships("B", 1, 9, "Down")
    ship4.check_map()
    ship4.put_in_map()

    ship5 = Ships("S", 3, 4, "Down")
    ship5.check_map()
    ship5.put_in_map()

    ship6 = Ships("D", 0, 9, "Left")
    ship6.check_map()
    ship6.put_in_map()

    ship7 = Ships("C", 9, 9, "Left")
    ship7.check_map()
    ship7.put_in_map()
    map_battle.print_map()

    while check_map_status() == False:
        x_val = int(input("Enter X Val"))
        y_val = int(input("Enter Y Val"))
        player_one_input.input_values(x_val, y_val)
        player_one_input.check_attmpt()
        map_battle.print_map()

    print("Game Over")


main()
