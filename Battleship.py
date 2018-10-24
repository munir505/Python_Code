Map_Battleship_Player_One = []
Map_Battleship_Player_Two = []


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

    def create_map2(self):
        map_element = "*"
        for x in range(self.map_size):
            map_line = []
            for y in range(self.map_size):
                map_line += map_element
            Map_Battleship_Player_Two.append(map_line)

    def print_map_one(self):
        for x in range(self.map_size):
            print(Map_Battleship_Player_One[x])

    def print_map_two(self):
        for x in range(self.map_size):
            print(Map_Battleship_Player_Two[x])


class Ships:
    # Types: pb, b, s, c
    # Start: location on board, needs to be array, Between 0 and 9
    # Orientation: Up, Down, Left, Right
    def __init__(self, ship_type, start_one, start_two, orientation, player_map_own):
        self.ship_type = ship_type
        self.start_one = start_one
        self.start_two = start_two
        self.orientation = orientation
        self.player_own_map = player_map_own

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
                    self.player_own_map[self.start_one - x][self.start_two] = ship_type
                if self.orientation == "Down":
                    self.player_own_map[self.start_one + x][self.start_two] = ship_type
                if self.orientation == "Left":
                    self.player_own_map[self.start_one][self.start_two - x] = ship_type
                if self.orientation == "Right":
                    self.player_own_map[self.start_one][self.start_two + x] = ship_type
        else:
            print("Enter Again ship " + ship_type + " in orientation " + self.orientation)


class PlayerInput:
    def __init__(self):
        self.x_val = 0
        self.y_val = 0
        self.other_map = []

    def input_values(self, x_value, y_value, other_player_map):
        self.x_val = x_value
        self.y_val = y_value
        self.other_map = other_player_map

    def check_attempt(self):
        if self.other_map[self.x_val][self.y_val] == "*" or self.other_map[self.x_val][self.y_val] == "~":
            print("Missed")
            return False
        elif self.other_map[self.x_val][self.y_val] != "*" or self.other_map[self.x_val][self.y_val] != "~":
            print("Player Hit")
            self.other_map[self.x_val][self.y_val] = "~"
            return True


pl_one = [["P", 0, 0, "Right"],
          ["P", 8, 1, "Right"],
          ["B", 1, 6, "Left"],
          ["B", 1, 9, "Down"],
          ["S", 3, 4, "Down"],
          ["D", 0, 9, "Left"],
          ["C", 9, 9, "Left"]
          ]

pl_two = [["P", 9, 9, "Left"],
          ["P", 9, 0, "Up"],
          ["B", 4, 8, "Left"],
          ["B", 5, 4, "Left"],
          ["S", 8, 7, "Up"],
          ["D", 8, 3, "Right"],
          ["C", 0, 9, "Left"]
          ]


class PlayerInit:
    def __init__(self):
        self.player_map = []

    def populate_map(self, player_map_own, pl_list):
        self.player_map = player_map_own
        for x in range(7):
            ship_name = str(x)
            ship_name = Ships(pl_list[x][0], pl_list[x][1], pl_list[x][2], pl_list[x][3], self.player_map)
            ship_name.check_map()
            ship_name.put_in_map()


def check_map_status():
    is_dead = False
    for x in range(10):
        for y in range(10):
            if Map_Battleship_Player_One[x][y] != "*" and Map_Battleship_Player_One[x][y] != "~":
                is_dead = True

    return is_dead


def main():
    map_battle = MapBattleship(10)
    map_battle.create_map()
    map_battle.create_map2()
    player_one_input = PlayerInput()
    player_two_input = PlayerInput()

    player_one_layout = PlayerInit()
    player_one_layout.populate_map(Map_Battleship_Player_One, pl_one)

    player_two_layout = PlayerInit()
    player_two_layout.populate_map(Map_Battleship_Player_Two, pl_two)

    print("Player One Map")
    map_battle.print_map_one()
    print("Player Two Map")
    map_battle.print_map_two()

    while check_map_status():
        print("Player One Turn")
        one_x_val = int(input("Enter X Val"))
        one_y_val = int(input("Enter Y Val"))
        player_one_input.input_values(one_x_val, one_y_val, Map_Battleship_Player_Two)
        player_one_input.check_attempt()
        map_battle.print_map_one()
        
        print("Player Two Turn")
        two_x_val = int(input("Enter X Val"))
        two_y_val = int(input("Enter Y Val"))
        player_two_input.input_values(two_x_val, two_y_val, Map_Battleship_Player_One)
        player_two_input.check_attempt()
        map_battle.print_map_two()

    print("Game Over")


main()
