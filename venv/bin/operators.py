#算符
class Operators:
    def __init__(self, operator):
        if operator == '+':
            self.operator = 1
        elif operator == '-':
            self.operator = 2
        elif operator == '*':
            self.operator = 3

    def __eq__(self, other):
        return self.operator == other.operator

    def val(self):
        return self.operator

    def change(self, value):
        self.operator = value

    def tostr(self):
        if self.operator == 1:
            return '+'
        elif self.operator == 2:
            return '-'
        elif self.operator == 3:
            return '*'

