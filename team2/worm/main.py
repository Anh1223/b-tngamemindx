import random
from bot_base import GardenBotBase

class GardenBot(GardenBotBase):
    def __init__(self, *args):
        GardenBotBase.__init__(self, *args)
        self.role = self.roles["WORM"]
    def get_name(self):
        return "WORM"
    def do_turn(self):
        b = 0
        c = 0
        up = 0
        down = 0
        right = 0
        left = 0
        max_control = 0
        control_2 = ["UP", "DOWN", "RIGHT", "LEFT"]
        allies_information = self.allies[1]
        if self.my_team == 0:
            for i in range(3):
                if c == 0:
                    b = 1
                c = 0
                if i == 3:
                    c = 1
                    b = 0
                if self.map[b][c]["type"] == self.tile_types["PUMPKIN"]:
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
                    if enemies_information["role"] == 0:
                        if self.x < self.map_width - 1:
                            if self.x + 1 == enemies_information["x"]:
                                right -= 7
                        if self.x - 1 == enemies_information["x"]:
                            left -= 7
                        if self.y < self.map_height - 1:
                            if self.y + 1 == enemies_information["y"]:
                                down -= 7
                        if self.y - 1 == enemies_information["y"]:
                            up -= 7
                    if enemies_information["role"] == 1:
                        if enemies_information["fruitCarrying"] != 0:
                            if enemies_information["x"] > self.x:
                                left += 3
                            if enemies_information["x"] < self.x:
                                right += 3
                            if enemies_information["y"] > self.y:
                                up += 3
                            if enemies_information["y"] < self.y:
                                down += 3
            elif  self.enemies == []:
                if self.x < self.map_width:
                    right += 1
                if self.y < self.map_height:
                    down += 1
            if allies_information["x"] - self.x > 2:
                right += 2
            if self.x - allies_information["x"]> 2:
                left += 2
            if allies_information["y"] - self.y > 2:
                down += 2
            if self.x - allies_information["y"] > 2:
                up += 2
            if self.x < self.map_width - 1:
                if self.map[self.x + 1][self.y]["type"]== self.tile_types["IMPASSABLE"]:
                    right -= 6
            if self.x > 0:
                if self.map[self.x - 1][self.y]["type"]== self.tile_types["IMPASSABLE"]:
                    left -= 6
            if self.y < self.map_height - 1:
                if self.map[self.x][self.y + 1]["type"]== self.tile_types["IMPASSABLE"]:
                    down -= 6
            if self.y > 0:
                if self.map[self.x][self.y - 1]["type"]== self.tile_types["IMPASSABLE"]:
                    up -= 6
            if self.y < self.map_height - 1:
                if self.map[self.x][self.y + 1]["type"] == self.tile_types["PUMPKIN"]:   
                    down += 2
            if self.x < self.map_width - 1:
                if self.map[self.x + 1][self.y]["type"] == self.tile_types["PUMPKIN"]:   
                    right += 2
            if self.x > 0:
                if self.map[self.x - 1][self.y]["type"] == self.tile_types["PUMPKIN"]:  
                    left += 2
            if self.y > 0:
                if self.map[self.x][self.y - 1]["type"] == self.tile_types["PUMPKIN"]:  
                    up += 2
            if self.y < self.map_height - 2:
                if self.map[self.x][self.y + 2]["type"] == self.tile_types["PUMPKIN"]:   
                    down += 2
            if self.x < self.map_width - 2:
                if self.map[self.x + 2][self.y]["type"] == self.tile_types["PUMPKIN"]:   
                    right += 2
            if self.x > 1:
                if self.map[self.x - 2][self.y]["type"] == self.tile_types["PUMPKIN"]:  
                    left += 2
            if self.y > 1:
                if self.map[self.x][self.y - 2]["type"] == self.tile_types["PUMPKIN"]:  
                    up += 2
        else:
            for i in range(3):
                if c == 0:
                    b = 1
                c = 0
                if i == 3:
                    c = 1
                    b = 0
                if self.map[self.map_width - 1 - b][self.map_height - 1 - c]["type"] == self.tile_types["TOMATO"]:
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
                    if enemies_information["role"] == 0:
                        if self.x < self.map_width - 1:
                            if self.x + 1 == enemies_information["x"]:
                                right -= 7
                        if self.x != 0:
                            if self.x - 1 == enemies_information["x"]:
                                left -= 7
                        if self.y < self.map_height - 1:
                            if self.y + 1 == enemies_information["y"]:
                                down -= 7
                        if self.y != 0:
                            if self.y - 1 == enemies_information["y"]:
                                up -= 7
                    if enemies_information["role"] == 1:
                        if enemies_information["fruitCarrying"] != 0:
                            if enemies_information["x"] > self.x:
                                left += 3
                            if enemies_information["x"] < self.x:
                                right += 3
                            if enemies_information["y"] > self.y:
                                up += 3
                            if enemies_information["y"] < self.y:
                                down += 3
            elif  self.enemies == []:
                if self.x > 0:
                    left += 1
                if self.y < 0:
                    up += 1
            if allies_information["x"] - self.x > 2:
                right += 2
            if self.x - allies_information["x"]> 2:
                left += 2
            if allies_information["y"] - self.y > 2:
                down += 2
            if self.x - allies_information["y"] > 2:
                up += 2
            if self.x < self.map_width - 1:
                if self.map[self.x + 1][self.y]["type"]== self.tile_types["IMPASSABLE"]:
                    right -= 6
            if self.x > 0:
                if self.map[self.x - 1][self.y]["type"]== self.tile_types["IMPASSABLE"]:
                    left -= 6
            if self.y < self.map_height - 1:
                if self.map[self.x][self.y + 1]["type"]== self.tile_types["IMPASSABLE"]:
                    down -= 6
            if self.y > 0:
                if self.map[self.x][self.y - 1]["type"]== self.tile_types["IMPASSABLE"]:
                    up -= 6
            if self.y < self.map_height - 1:
                if self.map[self.x][self.y + 1]["type"] == self.tile_types["TOMATO"]:   
                    down += 2
            if self.x < self.map_width - 1:
                if self.map[self.x + 1][self.y]["type"] == self.tile_types["TOMATO"]:   
                    right += 2
            if self.x > 0:
                if self.map[self.x - 1][self.y]["type"] == self.tile_types["TOMATO"]:  
                    left += 2
            if self.y > 0:
                if self.map[self.x][self.y - 1]["type"] == self.tile_types["TOMATO"]:  
                    up += 2
            if self.y < self.map_height - 2:
                if self.map[self.x][self.y + 2]["type"] == self.tile_types["TOMATO"]:   
                    down += 2
            if self.x < self.map_width - 2:
                if self.map[self.x + 2][self.y]["type"] == self.tile_types["TOMATO"]:   
                    right += 2
            if self.x > 1:
                if self.map[self.x - 2][self.y]["type"] == self.tile_types["TOMATO"]:  
                    left += 2
            if self.y > 1:
                if self.map[self.x][self.y - 2]["type"] == self.tile_types["TOMATO"]:  
                    up += 2
            
        control_1 = [up, down, right, left]
        for i in range(4):
            if max_control < control_1[i]:
                max_control = control_1[i]
        for i in range(4):
            if control_1[i] != max_control:
                if i == 0:
                    control_2.remove("UP")
                if i == 1:
                    control_2.remove("DOWN")
                if i == 2:
                    control_2.remove("RIGHT")
                if i == 3:
                    control_2.remove("LEFT")
        if len(control_2) == 0:
            control_2 = ["UP", "DOWN", "RIGHT", "LEFT"]
        random_1 = random.choice(control_2)
        #print("WORM", control_1)
        #print(random_1)
        return random_1
