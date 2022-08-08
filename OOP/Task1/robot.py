from copy import deepcopy


class robotStatus:
    ALIVE = 0
    DEAD  = 1
    CRASH = 2
    WATER = 3

BATTERY_VAL = 10
class robot:
    # mapa, x, y, bateria
    def __init__(self, T, x, y, b):
        self.__map = T
        self.__x = x
        self.__y = y
        self.__battery = b
        self.__status = robotStatus.ALIVE
        if T[x][y] == "G":
            self.__status = robotStatus.CRASH
        if T[x][y] == "W":
            self.__status = robotStatus.WATER
        if T[x][y] == "B":
            self.__set_battery(BATTERY_VAL)
            self.__set_map(x, y, "T")
        if self.__battery < 1:
            self.__status = robotStatus.DEAD
        

    def __isWall(self, T, x, y):
        if x < 0 or x >= len(T):
            return True
        if y < 0 or y >= len(T[x]):
            return True
        return False

    def __isMountain(self, T, x, y):
        return T[x][y]  == "G"

    def __isWater(self, T, x, y):
        return  T[x][y]  == "W"

    def __isBattery(self, T, x, y):
        return T[x][y]  == "B"


    def left(self, val = 1):
        if val < 0:
            return self
        if self.get_status == robotStatus.ALIVE:
            for _ in range(val):
                new_x = self.get_x()
                new_y = self.get_y() - 1
                self.__set_battery(-1)
                if self.__isWall(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.CRASH)
                    break
                elif self.__isMountain(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.CRASH)
                    break
                elif self.__isWater(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.WATER)
                    self.__set_y(-1)
                    break
                elif self.__isBattery(self.__get_curr_map(), new_x, new_y):
                    self.__set_battery(BATTERY_VAL)
                    self.__set_map(new_x, new_y, "T")
                    self.__set_y(-1)
                else:
                    self.__set_y(-1)
                if self.get_battery() <= 0:
                    self.__set_status(robotStatus.DEAD)
                    break
        return self

    def right(self, val = 1):
        if val < 0:
            return self
        if self.get_status == robotStatus.ALIVE:
            for _ in range(val):
                new_x = self.get_x()
                new_y = self.get_y() + 1
                self.__set_battery(-1)
                if self.__isWall(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.CRASH)
                    break
                elif self.__isMountain(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.CRASH)
                    break
                elif self.__isWater(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.WATER)
                    self.__set_y(1)
                    break
                elif self.__isBattery(self.__get_curr_map(), new_x, new_y):
                    self.__set_battery(BATTERY_VAL)
                    self.__set_map(new_x, new_y, "T")
                    self.__set_y(1)
                else:
                    self.__set_y(1)
                if self.get_battery() <= 0:
                    self.__set_status(robotStatus.DEAD)
                    break
        return self

    def up(self, val = 1):
        if val < 0:
            return self
        if self.get_status == robotStatus.ALIVE:
            for _ in range(val):
                new_x = self.get_x() + 1
                new_y = self.get_y()
                self.__set_battery(-1)
                if self.__isWall(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.CRASH)
                    break
                elif self.__isMountain(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.CRASH)
                    break
                elif self.__isWater(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.WATER)
                    self.__set_x(-1)
                    break
                elif self.__isBattery(self.__get_curr_map(), new_x, new_y):
                    self.__set_battery(BATTERY_VAL)
                    self.__set_map(new_x, new_y, "T")
                    self.__set_x(-1)
                else:
                    self.__set_x(-1)
                if self.get_battery() <= 0:
                    self.__set_status(robotStatus.DEAD)
                    break
        return self

    def down(self, val = 1):
        if val < 0:
            return self
        if self.get_status == robotStatus.ALIVE:
            for _ in range(val):
                new_x = self.get_x() + 1
                new_y = self.get_y()
                self.__set_battery(-1)
                if self.__isWall(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.CRASH)
                    break
                elif self.__isMountain(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.CRASH)
                    break
                elif self.__isWater(self.__get_curr_map(), new_x, new_y):
                    self.__set_status(robotStatus.WATER)
                    self.__set_x(1)
                    break
                elif self.__isBattery(self.__get_curr_map(), new_x, new_y):
                    self.__set_battery(BATTERY_VAL)
                    self.__set_map(new_x, new_y, "T")
                    self.__set_x(1)
                else:
                    self.__set_x(1)
                if self.get_battery() <= 0:
                    self.__set_status(robotStatus.DEAD)
                    break
        return self


    def __set_status(self, new_status):
        self.__status = new_status
        return

    def __set_battery(self, val):
        self.__battery += val
        return

    def __set_x(self, val):
        self.__x += val
        return

    def __set_y(self, val):
        self.__y += val
        return 

    def __set_map(self, x, y, val):
        self.__map[x][y] = val
        return

    def __get_curr_map(self):
        return self.__map


    def get_status(self):
        return self.__status

    def get_battery(self):
        return self.__battery


    def get_map(self):          
        output = deepcopy(self.__get_curr_map())
        if self.get_status() == robotStatus.ALIVE:
            output[self.get_x()][self.get_y()] = "R"
        else:
            output[self.get_x()][self.get_y()] = "X"
        return output

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y