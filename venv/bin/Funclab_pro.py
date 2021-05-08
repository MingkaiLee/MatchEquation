"""
本函数包为扩展到移动两根火柴的情况
本包的函数运行思路与Funclab包中相同，但写法存在出入

tenchanged和onechanged为对Funclab包中同名的函数进行重载，兼容了位数变化的情况
bitchange2为遍历移动某位，并且每次移动两根火柴
bitsub2和bitadd2为遍历移动某位，每次减去或加上两根火柴

selfchange2为数值元素自移，移动两根火柴
exchange2为数值元素间移动两根火柴

opchange为算符的自移，有"="与"*"的转换，"-"与"*"的转换

twoPeropr为利用Funclab包中的函数进行的部分状态空间搜索，特点是中间状态仍是合法表达式

twoPerop为搜索移动两根火柴的全部状态

Last edited time: 19. 10. 16
"""

from matchequation import MatchEquation
from Funclab import *
import copy


# 只改动十位的情况，覆盖Funclab中函数
def tenchanged(equation, val, sig, bit=0):
    new = copy.deepcopy(equation)
    if sig == 1:
        new.factor1.changeten(val)
        new.factor1.changebits(bit)
    elif sig == 2:
        new.factor2.changeten(val)
        new.factor2.changebits(bit)
    else:
        new.answer.changeten(val)
    new.isequal()
    return new


# 只改动个位的情况，覆盖Funclab中函数
def onechanged(equation, val, sig, bit=0):
    new = copy.deepcopy(equation)
    if sig == 1:
        new.factor1.changeone(val)
        new.factor1.changebits(bit)
    elif sig == 2:
        new.factor2.changeone(val)
        new.factor2.changebits(bit)
    else:
        new.answer.changeone(val)
    new.isequal()
    return new

#遍历移动某位，移动两根火柴
def bitchange2(closed, equation, sig, bit):
    #bit为2表示十位
    if bit == 2:
        while True:
            if equation.factorten(sig) == 0:
                # 原值为0，移动两根可变6或9
                if unvisited(closed, tenchanged(equation, 6, sig)):
                    closed.append(tenchanged(equation, 6, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 9, sig)):
                    closed.append(tenchanged(equation, 9, sig))
                    continue
                else:
                    break

            elif equation.factorten(sig) == 1:
                # 原值为1，移动两根不可变
                break

            elif equation.factorten(sig) == 2:
                # 原值为2，移动两根可变3或5
                if unvisited(closed, tenchanged(equation, 3, sig)):
                    closed.append(tenchanged(equation, 3, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 5, sig)):
                    closed.append(tenchanged(equation, 5, sig))
                    continue
                else:
                    break

            elif equation.factorten(sig) == 3:
                # 原值为3，移动两根可变2或5
                if unvisited(closed, tenchanged(equation, 2, sig)):
                    closed.append(tenchanged(equation, 2, sig))
                elif unvisited(closed, tenchanged(equation, 5, sig)):
                    closed.append(tenchanged(equation, 5, sig))
                else:
                    break

            elif equation.factorten(sig) == 4:
                # 原值为4，移动两根不可变
                break

            elif equation.factorten(sig) == 5:
                # 原值为5，移动两根可变2或3
                if unvisited(closed, tenchanged(equation, 2, sig)):
                    closed.append(tenchanged(equation, 2, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 3, sig)):
                    closed.append(tenchanged(equation, 3, sig))
                    continue
                else:
                    break

            elif equation.factorten(sig) == 6:
                # 原值为6，移动两根可变0或9
                if unvisited(closed, tenchanged(equation, 0, sig)):
                    closed.append(tenchanged(equation, 0, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 9, sig)):
                    closed.append(tenchanged(equation, 9, sig))
                    continue
                else:
                    break

            elif equation.factorten(sig) == 7:
                # 原值为7，移动两根不可变
                break

            elif equation.factorten(sig) == 8:
                # 原值为8，移动两根不可变
                break

            elif equation.factorten(sig) == 9:
                # 原值为9，移动两根可变0或6
                if unvisited(closed, tenchanged(equation, 0, sig)):
                    closed.append(tenchanged(equation, 0, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 6, sig)):
                    closed.append(tenchanged(equation, 6, sig))
                    continue
                else:
                    break

    else:
        while True:
            if equation.factorone(sig) == 0:
                # 原值为0，移动两根可变6或9
                if unvisited(closed, onechanged(equation, 6, sig)):
                    closed.append(onechanged(equation, 6, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 9, sig)):
                    closed.append(onechanged(equation, 9, sig))
                    continue
                else:
                    break

            elif equation.factorone(sig) == 1:
                # 原值为1，移动两根不可变
                break

            elif equation.factorone(sig) == 2:
                # 原值为2，移动两根可变3或5
                if unvisited(closed, onechanged(equation, 3, sig)):
                    closed.append(onechanged(equation, 3, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 5, sig)):
                    closed.append(onechanged(equation, 5, sig))
                    continue
                else:
                    break

            elif equation.factorone(sig) == 3:
                # 原值为3，移动两根可变2或5
                if unvisited(closed, onechanged(equation, 2, sig)):
                    closed.append(onechanged(equation, 2, sig))
                elif unvisited(closed, onechanged(equation, 5, sig)):
                    closed.append(onechanged(equation, 5, sig))
                else:
                    break

            elif equation.factorone(sig) == 4:
                # 原值为4，移动两根不可变
                break

            elif equation.factorone(sig) == 5:
                # 原值为5，移动两根可变2或3
                if unvisited(closed, onechanged(equation, 2, sig)):
                    closed.append(onechanged(equation, 2, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 3, sig)):
                    closed.append(onechanged(equation, 3, sig))
                    continue
                else:
                    break

            elif equation.factorone(sig) == 6:
                # 原值为6，移动两根可变0或9
                if unvisited(closed, onechanged(equation, 0, sig)):
                    closed.append(onechanged(equation, 0, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 9, sig)):
                    closed.append(onechanged(equation, 9, sig))
                    continue
                else:
                    break

            elif equation.factorone(sig) == 7:
                # 原值为7，移动两根不可变
                break

            elif equation.factorone(sig) == 8:
                # 原值为8，移动两根不可变
                break

            elif equation.factorone(sig) == 9:
                # 原值为9，移动两根可变0或6
                if unvisited(closed, onechanged(equation, 0, sig)):
                    closed.append(onechanged(equation, 0, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 6, sig)):
                    closed.append(onechanged(equation, 6, sig))
                    continue
                else:
                    break


#遍历移动某位，减两根火柴，新增变量bit标识是十位还是个位
def bitsub2(closed, equation, sig, bit):
    #bit为2表示十位
    if bit == 2:
        while True:
            if equation.factorten(sig) == 0:
                # 原值为0，减两根不可变
                break

            elif equation.factorten(sig) == 1:
                # 原值为1，减两根将变空
                if unvisited(closed, tenchanged(equation, 0, sig, 1)):
                    closed.append(tenchanged(equation, 0, sig, 1))
                break

            elif equation.factorten(sig) == 2:
                # 原值为2，减两根不可变
                break

            elif equation.factorten(sig) == 3:
                # 原值为3，减两根可变7
                if unvisited(closed, tenchanged(equation, 7, sig)):
                    closed.append(tenchanged(equation, 7, sig))
                break

            elif equation.factorten(sig) == 4:
                # 原值为4，减两根可变1
                if unvisited(closed, tenchanged(equation, 1, sig)):
                    closed.append(tenchanged(equation, 1, sig))
                break

            elif equation.factorten(sig) == 5:
                # 原值为5，减两根不可变
                break

            elif equation.factorten(sig) == 6:
                # 原值为6，减两根不可变
                break

            elif equation.factorten(sig) == 7:
                # 原值为7，减两根不可变
                break

            elif equation.factorten(sig) == 8:
                # 原值为8，减两根可变2, 3, 5
                if unvisited(closed, tenchanged(equation, 2, sig)):
                    closed.append(tenchanged(equation, 2, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 3, sig)):
                    closed.append(tenchanged(equation, 3, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 5, sig)):
                    closed.append(tenchanged(equation, 5, sig))
                    continue
                else:
                    break

            elif equation.factorten(sig) == 9:
                # 原值为9，减两根可变4
                if unvisited(closed, tenchanged(equation, 4, sig)):
                    closed.append(tenchanged(equation, 4, sig))
                    continue
                else:
                    break

    else:
        while True:
            if equation.factorone(sig) == 0:
                # 原值为0，减两根不可变
                break

            elif equation.factorone(sig) == 1:
                # 原值为1，减两根将变空
                if unvisited(closed, onechanged(equation, 0, sig, 1)):
                    closed.append(onechanged(equation, 0, sig, 1))
                break

            elif equation.factorone(sig) == 2:
                # 原值为2，减两根不可变
                break

            elif equation.factorone(sig) == 3:
                # 原值为3，减两根可变7
                if unvisited(closed, onechanged(equation, 7, sig)):
                    closed.append(onechanged(equation, 7, sig))
                break

            elif equation.factorone(sig) == 4:
                # 原值为4，减两根可变1
                if unvisited(closed, onechanged(equation, 1, sig)):
                    closed.append(onechanged(equation, 1, sig))
                break

            elif equation.factorone(sig) == 5:
                # 原值为5，减两根不可变
                break

            elif equation.factorone(sig) == 6:
                # 原值为6，减两根不可变
                break

            elif equation.factorone(sig) == 7:
                # 原值为7，减两根不可变
                break

            elif equation.factorone(sig) == 8:
                # 原值为8，减两根可变2, 3, 5
                if unvisited(closed, onechanged(equation, 2, sig)):
                    closed.append(onechanged(equation, 2, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 3, sig)):
                    closed.append(onechanged(equation, 3, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 5, sig)):
                    closed.append(onechanged(equation, 5, sig))
                    continue
                else:
                    break

            elif equation.factorone(sig) == 9:
                # 原值为9，减两根可变4
                if unvisited(closed, onechanged(equation, 4, sig)):
                    closed.append(onechanged(equation, 4, sig))
                    continue
                else:
                    break


#遍历移动某位，加两根火柴
def bitadd2(closed, equation, sig, bit):
    # bit为2表示十位
    if bit == 2:
        while True:
            if equation.factorten(sig) == 0:
                # 原值为0，加两根不可变
                break

            elif equation.factorten(sig) == 1:
                # 原值为1，加两根可变4
                if unvisited(closed, tenchanged(equation, 4, sig)):
                    closed.append(tenchanged(equation, 4, sig))
                break

            elif equation.factorten(sig) == 2:
                # 原值为2，加两根可变8
                if unvisited(closed, tenchanged(equation, 8, sig)):
                    closed.append(tenchanged(equation, 8, sig))
                break

            elif equation.factorten(sig) == 3:
                # 原值为3，加两根可变8
                if unvisited(closed, tenchanged(equation, 8, sig)):
                    closed.append(tenchanged(equation, 8, sig))
                break

            elif equation.factorten(sig) == 4:
                # 原值为4，加两根可变9
                if unvisited(closed, tenchanged(equation, 9, sig)):
                    closed.append(tenchanged(equation, 9, sig))
                break

            elif equation.factorten(sig) == 5:
                # 原值为5，加两根可变8
                if unvisited(closed, tenchanged(equation, 8, sig)):
                    closed.append(tenchanged(equation, 8, sig))
                break

            elif equation.factorten(sig) == 6:
                # 原值为6，加两根不可变
                break

            elif equation.factorten(sig) == 7:
                # 原值为7，加两根可变3
                if unvisited(closed, tenchanged(equation, 3, sig)):
                    closed.append(tenchanged(equation, 3, sig))
                break

            elif equation.factorten(sig) == 8:
                # 原值为8，加两根不可变
                break

            elif equation.factorten(sig) == 9:
                # 原值为9，加两根不可变
                break

    # bit为1表示个位
    elif bit == 1:
        while True:
            if equation.factorone(sig) == 0:
                # 原值为0，加两根不可变
                break

            elif equation.factorone(sig) == 1:
                # 原值为1，加两根可变4
                if unvisited(closed, onechanged(equation, 4, sig)):
                    closed.append(onechanged(equation, 4, sig))
                break

            elif equation.factorone(sig) == 2:
                # 原值为2，加两根可变8
                if unvisited(closed, onechanged(equation, 8, sig)):
                    closed.append(onechanged(equation, 8, sig))
                break

            elif equation.factorone(sig) == 3:
                # 原值为3，加两根可变8
                if unvisited(closed, onechanged(equation, 8, sig)):
                    closed.append(onechanged(equation, 8, sig))
                break

            elif equation.factorone(sig) == 4:
                # 原值为4，加两根可变9
                if unvisited(closed, onechanged(equation, 9, sig)):
                    closed.append(onechanged(equation, 9, sig))
                break

            elif equation.factorone(sig) == 5:
                # 原值为5，加两根可变8
                if unvisited(closed, onechanged(equation, 8, sig)):
                    closed.append(onechanged(equation, 8, sig))
                break

            elif equation.factorone(sig) == 6:
                # 原值为6，加两根不可变
                break

            elif equation.factorone(sig) == 7:
                # 原值为7，加两根可变3
                if unvisited(closed, onechanged(equation, 3, sig)):
                    closed.append(onechanged(equation, 3, sig))
                break

            elif equation.factorone(sig) == 8:
                # 原值为8，加两根不可变
                break

            elif equation.factorone(sig) == 9:
                # 原值为9，加两根不可变
                break

        # bit为其他，推荐为3，表示只有个位的数在前或后加一位为1
    else:
        # 1可加在原一位数的前后
        while True:
            temp = tenchanged(equation, equation.factorone(sig), sig, 2)
            temp = onechanged(temp, 1, sig)
            if unvisited(closed, temp):
                closed.append(temp)
                continue
            elif unvisited(closed, tenchanged(equation, 1, sig, 2)):
                closed.append(tenchanged(equation, 1, sig, 2))
                continue
            else:
                break


# 单个数值元素的自我改动
def selfchange2(closed, equation):
    # 创建一个中间列表存放中间态
    inters = []
    for x in range(1, 4):
        """
        在本循环中，完成所有自我改动，具体规则如下：
        存在两位的将自我改动，同时会发生位间改动
        由于输入要求只有有一位，所以各位总会自我改动
        """
        if equation.factorbits(x) == 2:
            bitchange2(closed, equation, x, 2)
            bitsub2(inters, equation, x, 2)
            for inter in inters:
                bitadd2(closed, inter, x, 1)
            inters.clear()
            bitadd2(inters, equation, x, 2)
            for inter in inters:
                bitsub2(closed, inter, x, 1)

        bitchange2(closed, equation, x, 1)


# 两个数值元素间的改动情况
def exchange2(closed, equation):
    # 创建一个中间列表存放中间态
    inters = []
    # factor1与factor2间的改动
    if equation.factorbits(1) == 2:
        bitsub2(inters, equation, 1, 2)
        for inter in inters:
            if equation.factorbits(2) == 2:
                bitadd2(closed, inter, 2, 2)
            bitadd2(closed, inter, 2, 1)
        inters.clear()

        bitadd2(inters, equation, 1, 2)
        for inter in inters:
            if equation.factorbits(2) == 2:
                bitsub2(closed, inter, 2, 2)
            bitsub2(closed, inter, 2, 1)
        inters.clear()

    bitsub2(inters, equation, 1, 1)
    for inter in inters:
        if equation.factorbits(2) == 2:
            bitadd2(closed, inter, 2, 2)
        bitadd2(closed, inter, 2, 1)
    inters.clear()

    bitadd2(inters, equation, 1, 1)
    for inter in inters:
        if equation.factorbits(2) == 2:
            bitsub2(closed, inter, 2, 2)
        bitsub2(closed, inter, 2, 1)
    inters.clear()

    # factor1与answer间的改动
    if equation.factorbits(1) == 2:
        bitsub2(inters, equation, 1, 2)
        for inter in inters:
            if equation.factorbits(3) == 2:
                bitadd2(closed, inter, 3, 2)
            bitadd2(closed, inter, 3, 1)
        inters.clear()

        bitadd2(inters, equation, 1, 2)
        for inter in inters:
            if equation.factorbits(3) == 2:
                bitsub2(closed, inter, 3, 2)
            bitsub2(closed, inter, 3, 1)
        inters.clear()

    bitsub2(inters, equation, 1, 1)
    for inter in inters:
        if equation.factorbits(3) == 2:
            bitadd2(closed, inter, 3, 2)
        bitadd2(closed, inter, 3, 1)
    inters.clear()

    bitadd2(inters, equation, 1, 1)
    for inter in inters:
        if equation.factorbits(3) == 2:
            bitsub2(closed, inter, 3, 2)
        bitsub2(closed, inter, 3, 1)
    inters.clear()

    # factor2与answer间的改动
    if equation.factorbits(2) == 2:
        bitsub2(inters, equation, 2, 2)
        for inter in inters:
            if equation.factorbits(3) == 2:
                bitadd2(closed, inter, 3, 2)
            bitadd2(closed, inter, 3, 1)
        inters.clear()

        bitadd2(inters, equation, 2, 2)
        for inter in inters:
            if equation.factorbits(3) == 2:
                bitsub2(closed, inter, 3, 2)
            bitsub2(closed, inter, 3, 1)
        inters.clear()

    bitsub2(inters, equation, 2, 1)
    for inter in inters:
        if equation.factorbits(3) == 2:
            bitadd2(closed, inter, 3, 2)
        bitadd2(closed, inter, 3, 1)
    inters.clear()

    bitadd2(inters, equation, 2, 1)
    for inter in inters:
        if equation.factorbits(3) == 2:
            bitsub2(closed, inter, 3, 2)
        bitsub2(closed, inter, 3, 1)
    inters.clear()

# 三个元素间的改动情况
def exchange3(closed, equation):
    inters1 = []
    inters2 = []
    if equation.factorbits(1) == 2:
        bitadd2(inters1, equation, 1, 2)
        for inter1 in inters1:
            onesub(inters2, inter1, 1)
        if equation.factorbits(2) == 2:
            for inter1 in inters1:
                tensub(inters2, inter1, 2)
        for inter1 in inters1:
            onesub(inters2, inter1, 2)
        if equation.factorbits(3) == 2:
            for inter1 in inters1:
                tensub(inters2, inter1, 3)
        for inter1 in inters1:
            onesub(inters2, inter1, 3)

        for inter2 in inters2:
            onesub(closed, inter2, 1)
        if equation.factorbits(2) == 2:
            for inter2 in inters2:
                tensub(closed, inter2, 2)
        for inter2 in inters2:
            onesub(closed, inter2, 2)
        if equation.factorbits(3) == 2:
            for inter2 in inters2:
                tensub(closed, inter2, 3)
        for inter2 in inters2:
            onesub(closed, inter2, 3)
        inters1.clear()
        inters2.clear()

        bitsub2(inters1, equation, 1, 2)
        for inter1 in inters1:
            oneadd(inters2, inter1, 1)
        if equation.factorbits(2) == 2:
            for inter1 in inters1:
                tenadd(inters2, inter1, 2)
        for inter1 in inters1:
            oneadd(inters2, inter1, 2)
        if equation.factorbits(3) == 2:
            for inter1 in inters1:
                tenadd(inters2, inter1, 3)
        for inter1 in inters1:
            oneadd(inters2, inter1, 3)

        for inter2 in inters2:
            oneadd(closed, inter2, 1)
        if equation.factorbits(2) == 2:
            for inter2 in inters2:
                tenadd(closed, inter2, 2)
        for inter2 in inters2:
            oneadd(closed, inter2, 2)
        if equation.factorbits(3) == 2:
            for inter2 in inters2:
                tenadd(closed, inter2, 3)
        for inter2 in inters2:
            oneadd(closed, inter2, 3)
        inters1.clear()
        inters2.clear()

    bitadd2(inters1, equation, 1, 1)
    if equation.factorbits(1) == 2:
        for inter1 in inters1:
            tensub(inters2, inter1, 1)
    if equation.factorbits(2) == 2:
        for inter1 in inters1:
            tensub(inters2, inter1, 2)
    for inter1 in inters1:
        onesub(inters2, inter1, 2)
    if equation.factorbits(3) == 2:
        for inter1 in inters1:
            tensub(inters2, inter1, 3)
    for inter1 in inters1:
        onesub(inters2, inter1, 3)

    if equation.factorbits(1) == 2:
        for inter2 in inters2:
            tensub(closed, inter2, 1)
    if equation.factorbits(2) == 2:
        for inter2 in inters2:
            tensub(closed, inter2, 2)
    for inter2 in inters2:
        onesub(closed, inter2, 2)
    if equation.factorbits(3) == 2:
        for inter2 in inters2:
            tensub(closed, inter2, 3)
    for inter2 in inters2:
        onesub(closed, inter2, 3)
    inters1.clear()
    inters2.clear()

    bitsub2(inters1, equation, 1, 1)
    if equation.factorbits(1) == 2:
        for inter1 in inters1:
            tenadd(inters2, inter1, 1)
    if equation.factorbits(2) == 2:
        for inter1 in inters1:
            tenadd(inters2, inter1, 2)
    for inter1 in inters1:
        oneadd(inters2, inter1, 2)
    if equation.factorbits(3) == 2:
        for inter1 in inters1:
            tenadd(inters2, inter1, 3)
    for inter1 in inters1:
        oneadd(inters2, inter1, 3)

    if equation.factorbits(1) == 2:
        for inter2 in inters2:
            tenadd(closed, inter2, 1)
    if equation.factorbits(2) == 2:
        for inter2 in inters2:
            tenadd(closed, inter2, 2)
    for inter2 in inters2:
        oneadd(closed, inter2, 2)
    if equation.factorbits(3) == 2:
        for inter2 in inters2:
            tenadd(closed, inter2, 3)
    for inter2 in inters2:
        oneadd(closed, inter2, 3)
    inters1.clear()
    inters2.clear()

    if equation.factorbits(2) == 2:
        bitadd2(inters1, equation, 2, 2)
        if equation.factorbits(1) == 2:
            for inter1 in inters1:
                tensub(inters2, inter1, 1)
        for inter1 in inters1:
            onesub(inters2, inter1, 1)
        for inter1 in inters1:
            onesub(inters2, inter1, 2)
        if equation.factorbits(3) == 2:
            for inter1 in inters1:
                tensub(inters2, inter1, 3)
        for inter1 in inters1:
            onesub(inters2, inter1, 3)

        if equation.factorbits(1) == 2:
            for inter2 in inters2:
                tensub(closed, inter2, 1)
        for inter2 in inters2:
            onesub(closed, inter2, 1)
        for inter2 in inters2:
            onesub(closed, inter2, 2)
        if equation.factorbits(3) == 2:
            for inter2 in inters2:
                tensub(closed, inter2, 3)
        for inter2 in inters2:
            onesub(closed, inter2, 3)
        inters1.clear()
        inters2.clear()

        bitsub2(inters1, equation, 1, 2)
        if equation.factorbits(1) == 2:
            for inter1 in inters1:
                tenadd(inters2, inter1, 1)
        for inter1 in inters1:
            oneadd(inters2, inter1, 1)
        for inter1 in inters1:
            oneadd(inters2, inter1, 2)
        if equation.factorbits(3) == 2:
            for inter1 in inters1:
                tenadd(inters2, inter1, 3)
        for inter1 in inters1:
            oneadd(inters2, inter1, 3)

        if equation.factorbits(1) == 2:
            for inter2 in inters2:
                tenadd(closed, inter2, 1)
        for inter2 in inters2:
            oneadd(closed, inter2, 1)
        for inter2 in inters2:
            oneadd(closed, inter2, 2)
        if equation.factorbits(3) == 2:
            for inter2 in inters2:
                tenadd(closed, inter2, 3)
        for inter2 in inters2:
            oneadd(closed, inter2, 3)
        inters1.clear()
        inters2.clear()

    bitadd2(inters1, equation, 2, 1)
    if equation.factorbits(1) == 2:
        for inter1 in inters1:
            tensub(inters2, inter1, 1)
    for inter1 in inters1:
        onesub(inters2, inter1, 1)
    if equation.factorbits(2) == 2:
        for inter1 in inters1:
            tensub(inters2, inter1, 2)
    if equation.factorbits(3) == 2:
        for inter1 in inters1:
            tensub(inters2, inter1, 3)
    for inter1 in inters1:
        onesub(inters2, inter1, 3)

    if equation.factorbits(1) == 2:
        for inter2 in inters2:
            tensub(closed, inter2, 1)
    for inter2 in inters2:
        onesub(closed, inter2, 1)
    if equation.factorbits(2) == 2:
        for inter2 in inters2:
            tensub(closed, inter2, 2)
    if equation.factorbits(3) == 2:
        for inter2 in inters2:
            tensub(closed, inter2, 3)
    for inter2 in inters2:
        onesub(closed, inter2, 3)
    inters1.clear()
    inters2.clear()

    bitsub2(inters1, equation, 1, 1)
    if equation.factorbits(1) == 2:
        for inter1 in inters1:
            tenadd(inters2, inter1, 1)
    for inter1 in inters1:
        oneadd(inters2, inter1, 1)
    if equation.factorbits(2) == 2:
        for inter1 in inters1:
            tenadd(inters2, inter1, 2)
    if equation.factorbits(3) == 2:
        for inter1 in inters1:
            tenadd(inters2, inter1, 3)
    for inter1 in inters1:
        oneadd(inters2, inter1, 3)

    if equation.factorbits(1) == 2:
        for inter2 in inters2:
            tenadd(closed, inter2, 1)
    for inter2 in inters2:
        oneadd(closed, inter2, 1)
    if equation.factorbits(2) == 2:
        for inter2 in inters2:
            tenadd(closed, inter2, 2)
    if equation.factorbits(3) == 2:
        for inter2 in inters2:
            tenadd(closed, inter2, 3)
    for inter2 in inters2:
        oneadd(closed, inter2, 3)
    inters1.clear()
    inters2.clear()

    if equation.factorbits(3) == 2:
        bitadd2(inters1, equation, 3, 2)
        if equation.factorbits(1) == 2:
            for inter1 in inters1:
                tensub(inters2, inter1, 1)
        for inter1 in inters1:
            onesub(inters2, inter1, 1)
        if equation.factorbits(2) == 2:
            for inter1 in inters1:
                tensub(inters2, inter1, 2)
        for inter1 in inters1:
            onesub(inters2, inter1, 2)
        for inter1 in inters1:
            onesub(inters2, inter1, 3)

        if equation.factorbits(1) == 2:
            for inter2 in inters2:
                tensub(closed, inter2, 1)
        for inter2 in inters2:
            onesub(closed, inter2, 1)
        if equation.factorbits(2) == 2:
            for inter2 in inters2:
                tensub(closed, inter2, 2)
        for inter2 in inters2:
            onesub(closed, inter2, 2)
        for inter2 in inters2:
            onesub(closed, inter2, 3)
        inters1.clear()
        inters2.clear()

        bitsub2(inters1, equation, 1, 2)
        if equation.factorbits(1) == 2:
            for inter1 in inters1:
                tenadd(inters2, inter1, 1)
        for inter1 in inters1:
            oneadd(inters2, inter1, 1)
        if equation.factorbits(2) == 2:
            for inter1 in inters1:
                tenadd(inters2, inter1, 2)
        for inter1 in inters1:
            oneadd(inters2, inter1, 2)
        for inter1 in inters1:
            oneadd(inters2, inter1, 3)

        if equation.factorbits(1) == 2:
            for inter2 in inters2:
                tenadd(closed, inter2, 1)
        for inter2 in inters2:
            oneadd(closed, inter2, 1)
        if equation.factorbits(2) == 2:
            for inter2 in inters2:
                tenadd(closed, inter2, 2)
        for inter2 in inters2:
            oneadd(closed, inter2, 2)
        for inter2 in inters2:
            oneadd(closed, inter2, 3)
        inters1.clear()
        inters2.clear()

    bitadd2(inters1, equation, 2, 1)
    if equation.factorbits(1) == 2:
        for inter1 in inters1:
            tensub(inters2, inter1, 1)
    for inter1 in inters1:
        onesub(inters2, inter1, 1)
    if equation.factorbits(2) == 2:
        for inter1 in inters1:
            tensub(inters2, inter1, 2)
    for inter1 in inters1:
        onesub(inters2, inter1, 2)
    if equation.factorbits(3) == 2:
        for inter1 in inters1:
            tensub(inters2, inter1, 3)

    if equation.factorbits(1) == 2:
        for inter2 in inters2:
            tensub(closed, inter2, 1)
    for inter2 in inters2:
        onesub(closed, inter2, 1)
    if equation.factorbits(2) == 2:
        for inter2 in inters2:
            tensub(closed, inter2, 2)
    for inter2 in inters2:
        onesub(closed, inter2, 2)
    if equation.factorbits(3) == 2:
        for inter2 in inters2:
            tensub(closed, inter2, 3)
    inters1.clear()
    inters2.clear()

    bitsub2(inters1, equation, 1, 1)
    if equation.factorbits(1) == 2:
        for inter1 in inters1:
            tenadd(inters2, inter1, 1)
    for inter1 in inters1:
        oneadd(inters2, inter1, 1)
    if equation.factorbits(2) == 2:
        for inter1 in inters1:
            tenadd(inters2, inter1, 2)
    for inter1 in inters1:
        oneadd(inters2, inter1, 2)
    if equation.factorbits(3) == 2:
        for inter1 in inters1:
            tenadd(inters2, inter1, 3)

    if equation.factorbits(1) == 2:
        for inter2 in inters2:
            tenadd(closed, inter2, 1)
    for inter2 in inters2:
        oneadd(closed, inter2, 1)
    if equation.factorbits(2) == 2:
        for inter2 in inters2:
            tenadd(closed, inter2, 2)
    for inter2 in inters2:
        oneadd(closed, inter2, 2)
    if equation.factorbits(3) == 2:
        for inter2 in inters2:
            tenadd(closed, inter2, 3)
    inters1.clear()
    inters2.clear()


# 算符的自我改动
def opchange(closed, equation):
    inters = []
    if equation.getoperator() == 1:
        closed.append(changeoperator(equation, 3))
    elif equation.getoperator() == 3:
        closed.append(changeoperator(equation, 1))
        for x in range(1, 4):
            if equation.factorbits(x) == 2:
                tenadd(inters, equation, x)
            oneadd(inters, equation, x)
            for inter in inters:
                if unvisited(closed, changeoperator(inter, 2)):
                    closed.append(changeoperator(inter, 2))
            inters.clear()

    elif equation.getoperator() == 2:
        for x in range(1, 4):
            if equation.factorbits(x) == 2:
                tensub(inters, equation, x)
            onesub(inters, equation, x)
            for inter in inters:
                if unvisited(closed, changeoperator(inter, 3)):
                    closed.append(changeoperator(inter, 3))
            inters.clear()



#求取移动两根火柴的部分状态空间函数，每次移动后的表达式都合理
def twoPeropr(closed, equation):
    inter = []
    for x in range(1, 4):
        selfchange(inter, equation, x)
        innerchange(inter, equation, x)
        exchange(inter, equation, x)
        facopchange(inter, equation, x)
    for equa in inter:
        for x in range(1, 4):
            selfchange(closed, equa, x)
            innerchange(closed, equa, x)
            exchange(closed, equa, x)
            facopchange(closed, equa, x)
    return closed


#求取移动两根火柴的全部可能状态空间函数
def twoPerop(equation):
    closed = [equation]
    twoPeropr(closed, equation)
    selfchange2(closed, equation)
    exchange3(closed, equation)
    exchange2(closed, equation)
    opchange(closed, equation)
    return closed






