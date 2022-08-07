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
        self.__map      = T
        self.__x        = x
        self.__y        = y
        self.__battery  = b
        self.__status = robotStatus.ALIVE
        if T[x][y] == "G":      self.__status = robotStatus.CRASH
        if T[x][y] == "W":      self.__status = robotStatus.WATER
        if T[x][y] == "B":
            self.__set_battery(BATTERY_VAL)
            self.__map[x][y] = "T"
        if self.__battery <= 0: 
            self.__status = robotStatus.DEAD
        pass

    def __isWall(self, T, x, y):
        output = False
        if x < 0:           output = True
        if y < 0:           output = True
        if x >= len(T):     output = True
        if y >= len(T[0]):  output = True
        return output

    def left(self, val = 1):
        x = self.get_x()
        y = self.get_y()
        b = self.get_battery()
        m = self.__map
        stat = self.get_status()
        if stat: return self
        if val <= 0: return self
        target = y - min(val, b)

        
        while y != target:
            y -= 1
            self.__battery -= 1
            if self.__isWall(m, x, y):
                self.__set_status(robotStatus.CRASH)
                return self
            if m[x][y] == "G":
                self.__y = y + 1
                self.__set_status(robotStatus.CRASH)
                return self
            if m[x][y] == "W":
                self.__set_status(robotStatus.WATER)
                self.__y = y
                return self
            if m[x][y] == "B":
                self.__set_map(x, y, "T")
                self.__set_battery(BATTERY_VAL)
            if self.__battery == 0:
                self.__set_status(robotStatus.DEAD)
                self.__y = y
                return self
        self.__y = target
        # Tutaj coś trzeba dodać                  
        return self     
    def right(self, val = 1):
        x = self.get_x()
        y = self.get_y()
        b = self.get_battery()
        m = self.__map
        stat = self.get_status()
        if stat: return self
        if val <= 0: return self
        target = y + min(val, b)

        
        while y != target:
            y += 1
            self.__battery -= 1
            if self.__isWall(m, x, y):
                self.__set_status(robotStatus.CRASH)
                return self
            if m[x][y] == "G":
                self.__set_status(robotStatus.CRASH)
                self.__y = y - 1
                return self
            if m[x][y] == "W":
                self.__set_status(robotStatus.WATER)
                self.__y = y
                return self
            if m[x][y] == "B":
                self.__set_map(x, y, "T")
                self.__set_battery(BATTERY_VAL)
            if self.__battery == 0:
                self.__set_status(robotStatus.DEAD)
                self.__y = y
                return self
        self.__y = target
        # Tutaj coś trzeba dodać                  
        return self  
    def up(self, val = 1):
        x = self.get_x()
        y = self.get_y()
        b = self.get_battery()
        m = self.__map
        stat = self.get_status()
        if stat: return self
        if val <= 0: return self
        target = x - min(val, b)

        
        while x != target:
            x -= 1
            self.__battery -= 1
            if self.__isWall(m, x, y):
                self.__set_status(robotStatus.CRASH)
                return self
            if m[x][y] == "G":
                self.__x = x + 1
                self.__set_status(robotStatus.CRASH)
                return self
            if m[x][y] == "W":
                self.__set_status(robotStatus.WATER)
                self.__x = x
                return self
            if m[x][y] == "B":
                self.__set_map(x, y, "T")
                self.__set_battery(BATTERY_VAL)
            if self.__battery == 0:
                self.__set_status(robotStatus.DEAD)
                self.__x = x
                return self
        self.__x = target
        # Tutaj coś trzeba dodać                  
        return self  
    def down(self, val = 1):
        x = self.get_x()
        y = self.get_y()
        b = self.get_battery()
        m = self.__map
        stat = self.get_status()
        if stat: return self
        if val <= 0: return self
        target = x + min(val, b)

        
        while x != target:
            x += 1
            self.__battery -= 1
            if self.__isWall(m, x, y):
                self.__set_status(robotStatus.CRASH)
                return self
            if m[x][y] == "G":
                self.__x = x - 1
                self.__set_status(robotStatus.CRASH)
                return self
            if m[x][y] == "W":
                self.__set_status(robotStatus.WATER)
                self.__x = x
                return self
            if m[x][y] == "B":
                self.__set_map(x, y, "T")
                self.__set_battery(BATTERY_VAL)
            if self.__battery == 0:
                self.__set_status(robotStatus.DEAD)
                self.__x =x
                return self
        self.__x = target
        # Tutaj coś trzeba dodać                  
        return self  

    def __set_status(self, stat):
        self.__status = stat
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

    def get_status(self):
        return self.__status
    def get_battery(self):
        return self.__battery
    def __get_u_map(self):
        return self.__map
    def get_map(self):
        output = deepcopy(self.__get_u_map())
        if self.get_status() == robotStatus.ALIVE:
            output[self.get_x()][self.get_y()] = "R"
        else:
            output[self.get_x()][self.get_y()] = "X"
        return output
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
