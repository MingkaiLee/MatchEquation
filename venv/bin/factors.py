#数值
class Factors:
    def __init__(self, value):
        #键值
        self.value = int(value)
        self.bits = len(value)
        if self.bits == 2:
            #十位
            self.ten = int(value[0])
            #个位
            self.one = int(value[1])
        else:
            self.ten = 0
            self.one = int(value)

    #重载使等号可用
    def __eq__(self, other):
            return self.value == other.value and self.bits == other.bits

    #返回个位值
    def getone(self):
        return self.one

    #返回十位值
    def getten(self):
        return self.ten

    #返回值
    def val(self):
        return self.value

    #修改十位
    def changeten(self, aim):
        self.ten = aim
        self.value = self.ten * 10 + self.one
        return True

    #修改个位
    def changeone(self, aim):
        self.one = aim
        self.value = self.ten * 10 + self.one
        return True

    #返回位数
    def getbits(self):
        return self.bits

    #修改位数
    def changebits(self, aim):
        if aim == 1:
            self.bits = self.bits - 1
        elif aim == 2:
            self.bits = self.bits + 1
        #当个位减位的情况
        if self.bits == 1 and self.ten != 0:
            self.one = self.ten
            self.ten = 0
            self.value = self.one

    #返回字符形式
    def tostr(self):
        if self.bits == 1:
            return str(self.one)
        elif self.bits == 2:
            return str(self.ten) + str(self.one)
        else:
            return ''
