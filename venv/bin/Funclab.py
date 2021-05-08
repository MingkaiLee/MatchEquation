#This package includes the function to change the sticks
"""
本函数包对应于只移动一根火柴的必做任务以及部分实现移动两根火柴的选做任务
其中，移动两根火柴的选做任务的两次移动中，表达式都是"合理的"
tenchanged和onechanged分别为只改动十位和个位的情况

tensub和tenadd为遍历改动十位
onesub和oneadd为遍历改动个位

selfsub返回一个中间式列表，为原式的数值减一根火柴
selfadd返回一个中间式列表，为原式的数值加一根火柴

selfchange和innerchange为一大类，该大类只对一个数字元素自身作改动
exchange为数值间进行一个火柴棒的转移
facopchange为数值和算符间进行火柴棒的转移

Last edited time: 19. 10. 04
"""
from matchequation import MatchEquation
import copy


#是否已在closed表中
def unvisited(closed, equation):
    if equation in closed:
        return False
    else:
        return True


#只改动十位的情况
def tenchanged(equation, val, sig):
    new = copy.deepcopy(equation)
    if sig == 1:
        new.factor1.changeten(val)
    elif sig == 2:
        new.factor2.changeten(val)
    else:
        new.answer.changeten(val)
    new.isequal()
    return new
    

#只改动个位的情况
def onechanged(equation, val, sig):
    new = copy.deepcopy(equation)
    if sig == 1:
        new.factor1.changeone(val)
    elif sig == 2:
        new.factor2.changeone(val)
    else:
        new.answer.changeone(val)
    new.isequal()
    return new


#改动算符的情况
def changeoperator(equation, val):
    new = copy.deepcopy(equation)
    new.operator.change(val)
    new.isequal()
    return new


#遍历改动十位,减一根火柴,为减少两位数数字间改变的重复编码而建立
def tensub(closed, inter, sig):
    while True:
        if inter.factorten(sig) == 0:
            #原值为0，减一根不可变
            break

        elif inter.factorten(sig) == 1:
            #原值为1，减一根不可变
            break

        elif inter.factorten(sig) == 2:
            #原值为2，减一根不可变
            break

        elif inter.factorten(sig) == 3:
            #原值为3，减一根不可变
            break

        elif inter.factorten(sig) == 4:
            #原值为4，减一根不可变
            break

        elif inter.factorten(sig) == 5:
            #原值为5，减一根不可变
            break

        elif inter.factorten(sig) == 6:
            #原值为6，减一根可变5
            if unvisited(closed, tenchanged(inter, 5, sig)):
                closed.append(tenchanged(inter, 5, sig))
                continue
            else:
                break

        elif inter.factorten(sig) == 7:
            #原值为7，减一根可变1
            if unvisited(closed, tenchanged(inter, 1, sig)):
                closed.append(tenchanged(inter, 1, sig))
                continue
            else:
                break

        elif inter.factorten(sig) == 8:
            #原值为8，减一根可变0，6，9
            if unvisited(closed, tenchanged(inter, 0, sig)):
                closed.append(tenchanged(inter, 0, sig))
                continue
            elif unvisited(closed, tenchanged(inter, 6, sig)):
                closed.append(tenchanged(inter, 6, sig))
                continue
            elif unvisited(closed, tenchanged(inter, 9, sig)):
                closed.append(tenchanged(inter, 9, sig))
                continue
            else:
                break

        elif inter.factorten(sig) == 9:
            #原值为9，减一根可变3，5
            if unvisited(closed, tenchanged(inter, 3, sig)):
                closed.append(tenchanged(inter, 3, sig))
                continue
            elif unvisited(closed, tenchanged(inter, 5, sig)):
                closed.append(tenchanged(inter, 5, sig))
                continue
            else:
                break


#遍历改动十位,加一根火柴,为减少两位数数字间改变的重复编码而建立
def tenadd(closed, inter, sig):
    while True:
        if inter.factorten(sig) == 0:
            #原值为0，加一根可变8
            if unvisited(closed, tenchanged(inter, 8, sig)):
                closed.append(tenchanged(inter, 8, sig))
                continue
            else:
                break

        elif inter.factorten(sig) == 1:
            #原值为1，加一根可变7
            if unvisited(closed, tenchanged(inter, 7, sig)):
                closed.append(tenchanged(inter, 7, sig))
                continue
            else:
                break

        elif inter.factorten(sig) == 2:
            #原值为2，加一根不可变
            break

        elif inter.factorten(sig) == 3:
            #原值为3，加一根可变9
            if unvisited(closed, tenchanged(inter, 9, sig)):
                closed.append(tenchanged(inter, 9, sig))
                continue
            else:
                break

        elif inter.factorten(sig) == 4:
            #原值为4，加一根不可变
            break

        elif inter.factorten(sig) == 5:
            #原值为5，加一根可变6，9
            if unvisited(closed, tenchanged(inter, 6, sig)):
                closed.append(tenchanged(inter, 6, sig))
                continue
            elif unvisited(closed, tenchanged(inter, 9 ,sig)):
                closed.append(tenchanged(inter, 9, sig))
                continue
            else:
                break

        elif inter.factorten(sig) == 6:
            #原值为6，加一根可变8
            if unvisited(closed, tenchanged(inter, 8, sig)):
                closed.append(tenchanged(inter, 8, sig))
                continue
            else:
                break

        elif inter.factorten(sig) == 7:
            #原值为7，加一根不可变
            break

        elif inter.factorten(sig) == 8:
            #原值为8，加一根不可变
            break

        else:
            #原值为9，加一根可变8
            if unvisited(closed, tenchanged(inter, 8, sig)):
                closed.append(tenchanged(inter, 8, sig))
                continue
            else:
                break


#遍历改动个位，减一根火柴
def onesub(closed, inter, sig):
    while True:
        if inter.factorone(sig) == 0:
            # 原值为0，减一根不可变
            break

        elif inter.factorone(sig) == 1:
            # 原值为1，减一根不可变
            break

        elif inter.factorone(sig) == 2:
            # 原值为2，减一根不可变
            break

        elif inter.factorone(sig) == 3:
            # 原值为3，减一根不可变
            break

        elif inter.factorone(sig) == 4:
            # 原值为4，减一根不可变
            break

        elif inter.factorone(sig) == 5:
            # 原值为5，减一根不可变
            break

        elif inter.factorone(sig) == 6:
            # 原值为6，减一根可变5
            if unvisited(closed, onechanged(inter, 5, sig)):
                closed.append(onechanged(inter, 5, sig))
                continue
            else:
                break

        elif inter.factorone(sig) == 7:
            # 原值为7，减一根可变1
            if unvisited(closed, onechanged(inter, 1, sig)):
                closed.append(onechanged(inter, 1, sig))
                continue
            else:
                break

        elif inter.factorone(sig) == 8:
            # 原值为8，减一根可变0，6，9
            if unvisited(closed, onechanged(inter, 0, sig)):
                closed.append(onechanged(inter, 0, sig))
                continue
            elif unvisited(closed, onechanged(inter, 6, sig)):
                closed.append(onechanged(inter, 6, sig))
                continue
            elif unvisited(closed, onechanged(inter, 9, sig)):
                closed.append(onechanged(inter, 9, sig))
                continue
            else:
                break

        elif inter.factorone(sig) == 9:
            # 原值为9，减一根可变3，5
            if unvisited(closed, onechanged(inter, 3, sig)):
                closed.append(onechanged(inter, 3, sig))
                continue
            elif unvisited(closed, onechanged(inter, 5, sig)):
                closed.append(onechanged(inter, 5, sig))
                continue
            else:
                break


#遍历改动个位，加一根火柴
def oneadd(closed, inter, sig):
    while True:
        if inter.factorone(sig) == 0:
            #原值为0，加一根可变8
            if unvisited(closed, onechanged(inter, 8, sig)):
                closed.append(onechanged(inter, 8, sig))
                continue
            else:
                break

        elif inter.factorone(sig) == 1:
            #原值为1，加一根可变7
            if unvisited(closed, onechanged(inter, 7, sig)):
                closed.append(onechanged(inter, 7, sig))
                continue
            else:
                break

        elif inter.factorone(sig) == 2:
            #原值为2，加一根不可变
            break

        elif inter.factorone(sig) == 3:
            #原值为3，加一根可变9
            if unvisited(closed, onechanged(inter, 9, sig)):
                closed.append(onechanged(inter, 9, sig))
                continue
            else:
                break

        elif inter.factorone(sig) == 4:
            #原值为4，加一根不可变
            break

        elif inter.factorone(sig) == 5:
            #原值为5，加一根可变6，9
            if unvisited(closed, onechanged(inter, 6, sig)):
                closed.append(onechanged(inter, 6, sig))
                continue
            elif unvisited(closed, onechanged(inter, 9 ,sig)):
                closed.append(onechanged(inter, 9, sig))
                continue
            else:
                break

        elif inter.factorone(sig) == 6:
            #原值为6，加一根可变8
            if unvisited(closed, onechanged(inter, 8, sig)):
                closed.append(onechanged(inter, 8, sig))
                continue
            else:
                break

        elif inter.factorone(sig) == 7:
            #原值为7，加一根不可变
            break

        elif inter.factorone(sig) == 8:
            #原值为8，加一根不可变
            break

        else:
            #原值为9，加一根可变8
            if unvisited(closed, onechanged(inter, 8, sig)):
                closed.append(onechanged(inter, 8, sig))
                continue
            else:
                break


#某个数字的自我改变的情况
def selfchange(closed, equation, sig):
    """
    signal值为1，2，3分别表示对factor1, factor2, answer的改动
    """
    if equation.factorbits(sig) == 1:
        while True:
            #原值为0，可自变为6或9
            if equation.factorone(sig) == 0:
                if unvisited(closed, onechanged(equation, 6, sig)):
                    closed.append(onechanged(equation, 6, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 9, sig)):
                    closed.append(onechanged(equation, 9, sig))
                    continue
                else:
                    break

            #原值为1，不可变
            elif equation.factorone(sig) == 1:
                break

            #原值为2，可变为3
            elif equation.factorone(sig) == 2:
                if unvisited(closed, onechanged(equation, 3, sig)):
                    closed.append(onechanged(equation, 3, sig))
                    continue
                else:
                    break

            #原值为3，可变为2或5
            elif equation.factorone(sig) == 3:
                if unvisited(closed, onechanged(equation, 2, sig)):
                    closed.append(onechanged(equation, 2, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 5, sig)):
                    closed.append(onechanged(equation, 5, sig))
                    continue
                else:
                    break

            #原值为4，不可变
            elif equation.factorone(sig) == 4:
                break

            #原值为5，可变为3
            elif equation.factorone(sig) == 5:
                if unvisited(closed, onechanged(equation, 3, sig)):
                    closed.append(onechanged(equation, 3, sig))
                    continue
                else:
                    break

            #原值为6，可变为0或9
            elif equation.factorone(sig) == 6:
                if unvisited(closed, onechanged(equation, 0, sig)):
                    closed.append(onechanged(equation, 0, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 9, sig)):
                    closed.append(onechanged(equation, 9, sig))
                    continue
                else:
                    break

            #原值为7，不可变
            elif equation.factorone(sig) == 7:
                break

            #原值为8，不可变
            elif equation.factorone(sig) == 8:
                break

            #原值为9，可变为0或6
            elif equation.factorone(sig) == 9:
                if unvisited(closed, onechanged(equation, 0, sig)):
                    closed.append(onechanged(equation, 0, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 6, sig)):
                    closed.append(onechanged(equation, 6, sig))
                    continue
                else:
                    break

    #两位数的情况
    else:
        #个位的变化
        while True:
            if equation.factorone(sig) == 0:
                if unvisited(closed, onechanged(equation, 6, sig)):
                    closed.append(onechanged(equation, 6, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 9, sig)):
                    closed.append(onechanged(equation, 9, sig))
                    continue
                else:
                    break

            # 原值为1，不可变
            elif equation.factorone(sig) == 1:
                break

            # 原值为2，可变为3
            elif equation.factorone(sig) == 2:
                if unvisited(closed, onechanged(equation, 3, sig)):
                    closed.append(onechanged(equation, 3, sig))
                    continue
                else:
                    break

            # 原值为3，可变为2或5
            elif equation.factorone(sig) == 3:
                if unvisited(closed, onechanged(equation, 2, sig)):
                    closed.append(onechanged(equation, 2, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 5, sig)):
                    closed.append(onechanged(equation, 5, sig))
                    continue
                else:
                    break

            # 原值为4，不可变
            elif equation.factorone(sig) == 4:
                break

            # 原值为5，可变为2或3
            elif equation.factorone(sig) == 5:
                if unvisited(closed, onechanged(equation, 3, sig)):
                    closed.append(onechanged(equation, 3, sig))
                    continue
                else:
                    break

            # 原值为6，可变为0或9
            elif equation.factorone(sig) == 6:
                if unvisited(closed, onechanged(equation, 0, sig)):
                    closed.append(onechanged(equation, 0, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 9, sig)):
                    closed.append(onechanged(equation, 9, sig))
                    continue
                else:
                    break

            # 原值为7，不可变
            elif equation.factorone(sig) == 7:
                break

            # 原值为8，不可变
            elif equation.factorone(sig) == 8:
                break

            # 原值为9，可变为0或6
            elif equation.factorone(sig) == 9:
                if unvisited(closed, onechanged(equation, 0, sig)):
                    closed.append(onechanged(equation, 0, sig))
                    continue
                elif unvisited(closed, onechanged(equation, 6, sig)):
                    closed.append(onechanged(equation, 6, sig))
                    continue
                else:
                    break

        while True:
            if equation.factorten(sig) == 0:
                if unvisited(closed, tenchanged(equation, 6, sig)):
                    closed.append(tenchanged(equation, 6, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 9, sig)):
                    closed.append(tenchanged(equation, 9, sig))
                    continue
                else:
                    break

            # 原值为1，不可变
            elif equation.factorten(sig) == 1:
                break

            # 原值为2，可变为3
            elif equation.factorten(sig) == 2:
                if unvisited(closed, tenchanged(equation, 3, sig)):
                    closed.append(tenchanged(equation, 3, sig))
                    continue
                else:
                    break

            # 原值为3，可变为2或5
            elif equation.factorten(sig) == 3:
                if unvisited(closed, tenchanged(equation, 2, sig)):
                    closed.append(tenchanged(equation, 2, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 5, sig)):
                    closed.append(tenchanged(equation, 5, sig))
                    continue
                else:
                    break

            # 原值为4，不可变
            elif equation.factorten(sig) == 4:
                break

            # 原值为5，可变为3
            elif equation.factorten(sig) == 5:
                if unvisited(closed, tenchanged(equation, 3, sig)):
                    closed.append(tenchanged(equation, 3, sig))
                    continue
                else:
                    break

            # 原值为6，可变为0或9
            elif equation.factorten(sig) == 6:
                if unvisited(closed, tenchanged(equation, 0, sig)):
                    closed.append(tenchanged(equation, 0, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 9, sig)):
                    closed.append(tenchanged(equation, 9, sig))
                    continue
                else:
                    break

            # 原值为7，不可变
            elif equation.factorten(sig) == 7:
                break

            # 原值为8，不可变
            elif equation.factorten(sig) == 8:
                break

            # 原值为9，可变为0或6
            elif equation.factorten(sig) == 9:
                if unvisited(closed, tenchanged(equation, 0, sig)):
                    closed.append(tenchanged(equation, 0, sig))
                    continue
                elif unvisited(closed, tenchanged(equation, 6, sig)):
                    closed.append(tenchanged(equation, 6, sig))
                    continue
                else:
                    break


#两位数的数字间改变的情况
def innerchange(closed, equation, sig):
    """
    signal的值为1, 2, 3分别表示对factor1, factor2, answer的改动
    该方法仅对有两位数的factor有效
    """
    if equation.factorbits(sig) == 2:
        #个位加一根，十位减一根
        while True:
            if equation.factorone(sig) == 0:
                """
                inter为中间产物，比原式的火柴总数多1
                """
                #原值为0，加一根可变为8
                inter = onechanged(equation, 8, sig)
                tensub(closed, inter, sig)
                break

            elif equation.factorone(sig) == 1:
                #原值为1，加一根可变为7
                inter = onechanged(equation, 7, sig)
                tensub(closed, inter, sig)
                break

            elif equation.factorone(sig) == 2:
                #原值为2，加一根不可变
                break

            elif equation.factorone(sig) == 3:
                #原值为3，加一根可变为9
                inter = onechanged(equation, 9, sig)
                tensub(closed, inter, sig)
                break

            elif equation.factorone(sig) == 4:
                #原值为4，加一根不可变
                break

            elif equation.factorone(sig) == 5:
                #原值为5，加一根可变为6，9
                inter = onechanged(equation, 6, sig)
                tensub(closed, inter, sig)
                inter = onechanged(equation, 9, sig)
                tensub(closed, inter, sig)
                break

            elif equation.factorone(sig) == 6:
                #原值为6，加一根可变为8
                inter = onechanged(equation, 8, sig)
                tensub(closed, inter, sig)
                break

            elif equation.factorone(sig) == 7:
                #原值为7，加一根不可变
                break

            elif equation.factorone(sig) == 8:
                #原值为8，加一根不可变
                break

            else:
                #原值为9，加一根可变为8
                inter  = onechanged(equation, 8, sig)
                tensub(closed, inter, sig)
                break

        #个位减一根十位加一根
        while True:
            if equation.factorone(sig) == 0:
                #原值为0，减一根不可变
                break

            elif equation.factorone(sig) == 1:
                #原值为1，减一根不可变
                break

            elif equation.factorone(sig) == 2:
                #原值为2，减一根不可变
                break

            elif equation.factorone(sig) == 3:
                #原值为3，减一根不可变
                break

            elif equation.factorone(sig) == 4:
                #原值为4，减一根不可变
                break

            elif equation.factorone(sig) == 5:
                #原值为5，减一根不可变
                break

            elif equation.factorone(sig) == 6:
                #原值为6，减一根可变5
                inter = onechanged(equation, 5, sig)
                tenadd(closed, inter, sig)
                break

            elif equation.factorone(sig) == 7:
                #原值为7，减一根可变1
                inter = onechanged(equation, 1, sig)
                tenadd(closed, inter, sig)
                break

            elif equation.factorone(sig) == 8:
                #原值为8，减一根可变0，6，9
                inter = onechanged(equation, 0, sig)
                tenadd(closed, inter, sig)
                inter = onechanged(equation, 6, sig)
                tenadd(closed, inter ,sig)
                inter = onechanged(equation, 9, sig)
                tenadd(closed, inter, sig)
                break

            else:
                #原值为9，减一根可变3，5
                inter = onechanged(equation, 3, sig)
                tenadd(closed, inter, sig)
                inter = onechanged(equation, 5, sig)
                tenadd(closed, inter, sig)
                break


#减一根火柴的结果
def selfsub(equation, sig):
    inters = []
    #一位数的情况
    if equation.factorbits(sig) == 1:
        onesub(inters, equation, sig)

    #两位数的情况
    else:
        tensub(inters, equation, sig)
        onesub(inters, equation, sig)

    return inters


#加一根火柴的结果
def selfadd(equation, sig):
    inters = []
    #一位数的情况
    if equation.factorbits(sig) == 1:
        oneadd(inters, equation, sig)

    #两位数的情况
    else:
        tenadd(inters, equation, sig)
        oneadd(inters, equation, sig)

    return inters


#三个数值间改变的情况
def exchange(closed, equation, mod):
    """
    :param closed: closed表
    :param equation: 原式
    :param mod: 模式，1为factor1和factor2间交换火柴，2为factor1和answer间交换火柴，3位factor2和answer间交换火柴
    """
    if mod == 1:
        #factor1加一根，factor2减一根
        inters = selfadd(equation, 1)
        for inter in inters:
            finals = selfsub(inter, 2)
            for final in finals:
                if unvisited(closed, final):
                    closed.append(final)

        #factor1减一根，factor2加一根
        inters = selfsub(equation, 1)
        for inter in inters:
            finals = selfadd(inter, 2)
            for final in finals:
                if unvisited(closed, final):
                    closed.append(final)

    elif mod == 2:
        #factor1加一根，answer减一根
        inters = selfadd(equation, 1)
        for inter in inters:
            finals = selfsub(inter, 3)
            for final in finals:
                if unvisited(closed, final):
                    closed.append(final)

        #factor1减一根，answer加一根
        inters = selfsub(equation, 1)
        for inter in inters:
            finals = selfadd(inter, 3)
            for final in finals:
                if unvisited(closed, final):
                    closed.append(final)

    else:
        #factor2加一根，answer减一根
        inters = selfadd(equation, 2)
        for inter in inters:
            finals = selfsub(inter, 3)
            for final in finals:
                if unvisited(closed, final):
                    closed.append(final)

        #factor2减一根，answer加一根
        inters = selfsub(equation, 2)
        for inter in inters:
            finals = selfadd(inter, 3)
            for final in finals:
                if unvisited(closed, final):
                    closed.append(final)


#数值和算符间转移的情况
def facopchange(closed, equation, sig):
    #加只能变减
    if equation.getoperator() == 1:
        inter = changeoperator(equation, 2)
        finals = selfadd(inter, sig)
        for final in finals:
            if unvisited(closed, final):
                closed.append(final)

    #减只能变加
    elif equation.getoperator() == 2:
        inter = changeoperator(equation, 1)
        finals = selfsub(inter, sig)
        for final in finals:
            if unvisited(closed, final):
                closed.append(final)


#求取只移动一根火柴的全部可能状态空间函数
def onePerop(equation):
    closed = [equation]
    for x in range(1, 4):
        selfchange(closed, equation, x)
        innerchange(closed, equation, x)
        exchange(closed, equation, x)
        facopchange(closed, equation, x)
    return closed

