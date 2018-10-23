Map_Battleship = []


class MapBattleship:
    def __init__(self, map_size):
        self.map_size = map_size

    def create_map(self):
        map_element = "*"
        for x in range(self.map_size):
            map_line = []
            for y in range(self.map_size):
                map_line += map_element
            Map_Battleship.append(map_line)

    def print_map(self):
        for x in range(self.map_size):
            print(Map_Battleship[x])


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
        if self.ship_type == "patrol_boat":
            return 2
        if self.ship_type == "battleship":
            return 3
        if self.ship_type == "submarine":
            return 3
        if self.ship_type == "destroyer":
            return 4
        if self.ship_type == "carrier":
            return 5

    def check_map(self):
        place = False
        if self.orientation == "Up":
            if self.start_one - self.get_length(self) < 0:
                print("Error")
            else:
                place = True

        if self.orientation == "Down":
            if self.start_one + self.get_length(self) > 9:
                print("Error")
            else:
                place = True

        if self.orientation == "Left":
            if self.start_two + self.get_length(self) < 0:
                print("Error")
            else:
                place = True

        if self.orientation == "Right":
            if self.start_two + self.get_length(self) > 9:
                print("Error")
            else:
                place = True

        if place == True:
            return True
        else:
            return False

        def put_in_map():
            print(self.check_map())


Map = MapBattleship(10)
Map.create_map()
# Map.print_map()

ship1 = Ships("patrol_boat", 5, 5, "Up")
ship1.check_map()
ship1.put_in_map()
