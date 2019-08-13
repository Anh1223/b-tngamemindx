import random
from bot_base import GardenBotBase

class GardenBot(GardenBotBase):
    def __init__(self, *args):
        GardenBotBase.__init__(self, *args)
        self.role = self.roles["HARVESTER"]
    def get_name(self):
        return "HARVESTER"

    def do_start(self):
        return

    def do_turn(self):
        up = 0
        down = 0
        right = 0
        left = 0
        max_control = 0
        control_2 = ["UP", "DOWN", "RIGHT", "LEFT"]
        if self.x < self.map_width - 1:
            if self.map[self.x + 1][self.y]["type"]== self.tile_types["IMPASSABLE"]:
                right -= 11
        if self.x > 0:
            if self.map[self.x - 1][self.y]["type"]== self.tile_types["IMPASSABLE"]:
                left -= 11
        if self.y < self.map_height - 1:
            if self.map[self.x][self.y + 1]["type"]== self.tile_types["IMPASSABLE"]:
                down -= 11
        if self.y > 0:
            if self.map[self.x][self.y - 1]["type"]== self.tile_types["IMPASSABLE"]:
                up -= 11
        if self.enemies != []:
                for i in self.enemies:
                    enemies_information = i
                    if enemies_information["role"] == 2:
                        if self.x < self.map_width - 1:
                            if self.x + 1 == enemies_information["x"]:
                                right -= 11
                        if self.x > 0:
                            if self.x - 1 == enemies_information["x"]:
                                left -= 11
                        if self.y < self.map_height - 1:
                            if self.y + 1 == enemies_information["y"]:
                                down -= 11
                        if self.y > 0:
                            if self.y - 1 == enemies_information["y"]:
                                up -= 11
                        if self.x < self.map_width - 2:
                            if self.x + 2 == enemies_information["x"]:
                                right -= 2
                        if self.x > 1:
                            if self.x - 2 == enemies_information["x"]:
                                left -= 2
                        if self.y < self.map_height - 1:
                            if self.y + 2 == enemies_information["y"]:
                                down -= 2
                        if self.y > 1:
                            if self.y - 2 == enemies_information["y"]:
                                up -= 2
                        if self.x < self.map_width - 1 and self.y < self.map_height - 1:
                            if self.x + 1 == enemies_information["x"] and self.y + 1 == enemies_information["y"]:
                                down -= 11
                                left -= 11
                        if self.x > 0 and self.y < self.map_height - 1:
                            if self.x - 1 == enemies_information["x"] and self.y + 1 == enemies_information["y"]:
                                down -= 11
                                right -= 11
                        if self.x < self.map_width - 1 and self.y > 0:
                            if self.y - 1 == enemies_information["y"] and self.x + 1 == enemies_information["x"]:
                                up -= 11
                                left -= 11
                        if self.y > 0 and self.x > 0:
                            if self.y - 1 == enemies_information["y"] and self.x - 1 == enemies_information["x"]:
                                up -= 11
                                right -= 11
        if self.my_team == 0:
            if self.state["fruitCarrying"] > self.game_rule["harvesterMaxCapacity"] // 2:
                up += 1
                left += 1
            if self.state["fruitCarrying"] < self.game_rule["harvesterMaxCapacity"]:
                if self.y < self.map_height - 1:
                    if self.map[self.x][self.y + 1]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x][self.y + 1]["growState"] >= self.game_rule["wildberryFruitTime"]:
                            down += 3
                if self.x < self.map_width - 1:
                    if self.map[self.x + 1][self.y]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x + 1][self.y]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            right += 3
                if self.x > 0:
                    if self.map[self.x - 1][self.y]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x - 1][self.y]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            left += 3
                if self.y > 0:
                    if self.map[self.x][self.y - 1]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x][self.y - 1]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            up += 3
                if self.y < self.map_height - 1:
                    if self.map[self.x][self.y + 1]["type"] == self.tile_types["TOMATO"]:
                        if self.map[self.x][self.y + 1]["growState"] >= self.game_rule["plantFruitTime"]:    
                            down += 2
                if self.x < self.map_width - 1:
                    if self.map[self.x + 1][self.y]["type"] == self.tile_types["TOMATO"]:
                        if self.map[self.x + 1][self.y]["growState"] >= self.game_rule["plantFruitTime"]:    
                            right += 2
                if self.x > 0:
                    if self.map[self.x - 1][self.y]["type"] == self.tile_types["TOMATO"]:
                        if self.map[self.x - 1][self.y]["growState"] >= self.game_rule["plantFruitTime"]:    
                            left += 2
                if self.y > 0:
                    if self.map[self.x][self.y - 1]["type"] == self.tile_types["TOMATO"]:
                        if self.map[self.x][self.y - 1]["growState"] >= self.game_rule["plantFruitTime"]:    
                            up += 2


                if self.y < self.map_height - 2:
                    if self.map[self.x][self.y + 2]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x][self.y + 2]["growState"] >= self.game_rule["wildberryFruitTime"]:
                            down += 3
                if self.x < self.map_width - 2:
                    if self.map[self.x + 2][self.y]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x + 2][self.y]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            right += 3
                if self.x > 1:
                    if self.map[self.x - 2][self.y]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x - 2][self.y]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            left += 3
                if self.y > 1:
                    if self.map[self.x][self.y - 2]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x][self.y - 2]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            up += 3
                if self.y < self.map_height - 2:
                    if self.map[self.x][self.y + 2]["type"] == self.tile_types["TOMATO"]:
                        if self.map[self.x][self.y + 2]["growState"] >= self.game_rule["plantFruitTime"]:    
                            down += 2
                if self.x < self.map_width - 2:
                    if self.map[self.x + 2][self.y]["type"] == self.tile_types["TOMATO"]:
                        if self.map[self.x + 2][self.y]["growState"] >= self.game_rule["plantFruitTime"]:    
                            right += 2
                if self.x > 1:
                    if self.map[self.x - 2][self.y]["type"] == self.tile_types["TOMATO"]:
                        if self.map[self.x - 2][self.y]["growState"] >= self.game_rule["plantFruitTime"]:    
                            left += 2
                if self.y > 1:
                    if self.map[self.x][self.y - 2]["type"] == self.tile_types["TOMATO"]:
                        if self.map[self.x][self.y - 2]["growState"] >= self.game_rule["plantFruitTime"]:    
                            up += 2
            else:
                if self.x > self.y:
                    left += 10
                if self.y > self.x:
                    up += 10
        else:
            if self.state["fruitCarrying"] > self.game_rule["harvesterMaxCapacity"] // 2:
                down += 1
                right += 1
            if self.state["fruitCarrying"] < self.game_rule["harvesterMaxCapacity"]:
                if self.y < self.map_height - 1:
                    if self.map[self.x][self.y + 1]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x][self.y + 1]["growState"] >= self.game_rule["wildberryFruitTime"]:
                            down += 3
                if self.x < self.map_width - 1:
                    if self.map[self.x + 1][self.y]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x + 1][self.y]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            right += 3
                if self.x > 0:
                    if self.map[self.x - 1][self.y]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x - 1][self.y]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            left += 3
                if self.y > 0:
                    if self.map[self.x][self.y - 1]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x][self.y - 1]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            up += 3
                if self.y < self.map_height - 1:
                    if self.map[self.x][self.y + 1]["type"] == self.tile_types["PUMPKIN"]:
                        if self.map[self.x][self.y + 1]["growState"] >= self.game_rule["plantFruitTime"]:    
                            down += 2
                if self.x < self.map_width - 1:
                    if self.map[self.x + 1][self.y]["type"] == self.tile_types["PUMPKIN"]:
                        if self.map[self.x + 1][self.y]["growState"] >= self.game_rule["plantFruitTime"]:    
                            right += 2
                if self.x > 0:
                    if self.map[self.x - 1][self.y]["type"] == self.tile_types["PUMPKIN"]:
                        if self.map[self.x - 1][self.y]["growState"] >= self.game_rule["plantFruitTime"]:    
                            left += 2
                if self.y > 0:
                    if self.map[self.x][self.y - 1]["type"] == self.tile_types["PUMPKIN"]:
                        if self.map[self.x][self.y - 1]["growState"] >= self.game_rule["plantFruitTime"]:    
                            up += 2


                if self.y < self.map_height - 2:
                    if self.map[self.x][self.y + 2]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x][self.y + 2]["growState"] >= self.game_rule["wildberryFruitTime"]:
                            down += 3
                if self.x < self.map_width - 2:
                    if self.map[self.x + 2][self.y]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x + 2][self.y]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            right += 3
                if self.x > 1:
                    if self.map[self.x - 2][self.y]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x - 2][self.y]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            left += 3
                if self.y > 1:
                    if self.map[self.x][self.y - 2]["type"] == self.tile_types["WILDBERRY"]:
                        if self.map[self.x][self.y - 2]["growState"] >= self.game_rule["wildberryFruitTime"]:    
                            up += 3
                if self.y < self.map_height - 2:
                    if self.map[self.x][self.y + 2]["type"] == self.tile_types["PUMPKIN"]:
                        if self.map[self.x][self.y + 2]["growState"] >= self.game_rule["plantFruitTime"]:    
                            down += 2
                if self.x < self.map_width - 2:
                    if self.map[self.x + 2][self.y]["type"] == self.tile_types["PUMPKIN"]:
                        if self.map[self.x + 2][self.y]["growState"] >= self.game_rule["plantFruitTime"]:    
                            right += 2
                if self.x > 1:
                    if self.map[self.x - 2][self.y]["type"] == self.tile_types["PUMPKIN"]:
                        if self.map[self.x - 2][self.y]["growState"] >= self.game_rule["plantFruitTime"]:    
                            left += 2
                if self.y > 1:
                    if self.map[self.x][self.y - 2]["type"] == self.tile_types["PUMPKIN"]:
                        if self.map[self.x][self.y - 2]["growState"] >= self.game_rule["plantFruitTime"]:    
                            up += 2
            else:
                if self.x < self.map_width -1:
                    right += 10
                if self.y < self.map_height - 1:
                    down += 10
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
        print("HARVESTER", control_1)
        #print(random_1)
        print(self.current_turn)
        return random_1