import random
from bot_base import GardenBotBase


class GardenBot(GardenBotBase):
    def __init__(self, *args):
        GardenBotBase.__init__(self, *args)
        self.role = self.roles["PLANTER"]
    def get_name(self):
        return "PLANTER"
    def do_turn(self):
        a = 0
        b = 1
        c = 1
        max_control = 0
        up = 0
        down = 0
        right = 0
        left = 0
        control_1 = [up, down, right, left]
        control_2 = ["UP", "DOWN", "RIGHT", "LEFT"]
        allies_information = self.allies[1]
        if self.is_scared == True:
            if allies_information["x"] > self.x:
                right += 1
            if allies_information["x"] < self.x:
                left += 1
            if allies_information["y"] > self.y:
                up += 1
            if allies_information["y"] < self.y:
                down += 1
        else:
            if self.my_team == 0:
                for i in range(3):
                    if c == 0:
                        b = 1
                    c = 0
                    if i == 3:
                        c = 1
                        b = 0
                    if self.map[b][c]["type"] == self.tile_types["EMPTY"]:
                        if self.x > b:
                            left += 2
                        if self.y > c:
                            up += 2
                        if self.x < b:
                            right += 2
                        if self.y < c:
                            down += 2
            else:
                for i in range(3):
                    if c == 0:
                        b = 1
                    c = 0
                    if i == 3:
                        c = 1
                        b = 0
                    if self.map[self.map_width - 1 - b][self.map_height - 1  - c]["type"] == self.tile_types["EMPTY"]:
                        if self.x > b:
                            left += 2
                        if self.y > c:
                            up += 2
                        if self.x < b:
                            right += 2
                        if self.y < c:
                            down += 2
            if self.enemies != []:
                for i in self.enemies:
                    enemies_information = i
                    if enemies_information["role"] == 2:
                        if enemies_information["x"] > self.x:
                            right += 1
                        if enemies_information["x"] < self.x:
                            left += 1
                        if enemies_information["y"] > self.y:
                            up += 1
                        if enemies_information["y"] < self.y:
                            down += 1
            if self.y < self.map_height - 1:
                if self.map[self.x][self.y + 1]["type"] == self.tile_types["EMPTY"]:
                    down += 1
            if self.x < self.map_width - 1:
                if self.map[self.x + 1][self.y]["type"] == self.tile_types["EMPTY"]:
                    right += 1
            if self.y > 0:
                if self.map[self.x][self.y - 1]["type"] == self.tile_types["EMPTY"]:
                    up += 1
            if self.x > 0:
                if self.map[self.x - 1][self.y]["type"] == self.tile_types["EMPTY"]:
                    left += 1
            if self.y < self.map_height - 2:
                if self.map[self.x][self.y + 2]["type"] == self.tile_types["EMPTY"]:
                    down += 1
            if self.x < self.map_width - 2:
                if self.map[self.x + 2][self.y]["type"] == self.tile_types["EMPTY"]:
                    right += 1
            if self.y > 1:
                if self.map[self.x][self.y - 2]["type"] == self.tile_types["EMPTY"]:
                    up += 1
            if self.x > 1:
                if self.map[self.x - 2][self.y]["type"] == self.tile_types["EMPTY"]:
                    left += 1
        if allies_information["x"] - self.x > 2:
            right += 3
        if self.x - allies_information["x"]> 2:
            left += 3
        if allies_information["x"] - self.y > 2:
            down += 3
        if self.x - allies_information["x"] > 2:
            up += 3
        if self.y < self.map_height - 1:
            if self.map[self.x][self.y + 1]["type"] == self.tile_types["IMPASSABLE"]:
                down -= 4
        if self.x < self.map_width - 1:
            if self.map[self.x + 1][self.y]["type"] == self.tile_types["IMPASSABLE"]:
                right -= 4
        if self.y > 0:
            if self.map[self.x][self.y - 1]["type"] == self.tile_types["IMPASSABLE"]:
                    up -= 4
        if self.x > 0:
            if self.map[self.x - 1][self.y]["type"] == self.tile_types["IMPASSABLE"]:
                left -= 4
        for i in range(4):
            if max_control < control_1[i]:
                max_control = control_1[i]
        for i in control_1:
            a += 1
            if i != max_control:
                if a == 1:
                    control_2.remove("UP")
                elif a == 2:
                    control_2.remove("DOWN")
                elif a == 3:
                    control_2.remove("RIGHT")
                elif a == 4:
                    control_2.remove("LEFT")
        if len(control_2) == 0:
            control_2 = ["UP", "DOWN", "RIGHT", "LEFT"]
        random_1 = random.choice(control_2)
        #print("PLANTER", control_1)
        #print(random_1)
        return random_1