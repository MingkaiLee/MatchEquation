from factors import Factors
from operators import Operators


class MatchEquation:
    def __init__(self, factor1='0', factor2='0', answer='0', operator='+'):
        #因子1
        self.factor1 = Factors(factor1)
        #因子2
        self.factor2 = Factors(factor2)
        #结果
        self.answer = Factors(answer)
        #符号
        self.operator = Operators(operator)
        #是否为等式
        if self.operator.val() == 1:
            if self.factor1.val() + self.factor2.val() == self.answer.val():
                self.equal = True
            else:
                self.equal = False
        elif self.operator.val() == 2:
            if self.factor1.val() - self.factor2.val() == self.answer.val():
                self.equal = True
            else:
                self.equal = False
        else:
            if self.factor1.val() * self.factor2.val() == self.answer.val():
                self.equal = True
            else:
                self.equal = False

    #重载使判等可用
    def __eq__(self, other):
        return (self.factor1 == other.factor1 and
                self.factor2 == other.factor2 and
                self.answer == other.answer and
                self.operator == other.operator
                )

    #用于修改后重新判等
    def isequal(self):
        if self.operator.val() == 1:
            if self.factor1.val() + self.factor2.val() == self.answer.val():
                self.equal = True
            else:
                self.equal = False
        elif self.operator.val() == 2:
            if self.factor1.val() - self.factor2.val() == self.answer.val():
                self.equal = True
            else:
                self.equal = False
        else:
            if self.factor1.val() * self.factor2.val() == self.answer.val():
                self.equal = True
            else:
                self.equal = False

    #返回算符
    def getoperator(self):
        return self.operator.val()

    #根据参数返回各项的个位值
    def factorone(self, sig):
        if sig == 1:
            return self.factor1.getone()
        elif sig == 2:
            return self.factor2.getone()
        else:
            return self.answer.getone()

    #根据参数返回各项的十位值
    def factorten(self, sig):
        if sig == 1:
            return self.factor1.getten()
        elif sig == 2:
            return self.factor2.getten()
        else:
            return self.answer.getten()

    #根据参数返回各项位数
    def factorbits(self, sig):
        if sig == 1:
            return self.factor1.getbits()
        elif sig == 2:
            return self.factor2.getbits()
        else:
            return self.answer.getbits()

    def showequation(self):
        eqstring = self.factor1.tostr() + self.operator.tostr() + self.factor2.tostr() + '=' + self.answer.tostr()
        print(eqstring)
        return eqstring

