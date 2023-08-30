MIN_VAL = -9223372036854775808
MAX_VAL = 9223372036854775807
class JavaLong:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        result = self.value + other.value
        if not MIN_VAL <= result <= MAX_VAL:
            result -= MIN_VAL * -2
        return JavaLong(result)

    def __mul__(self, other):
        result = self.value * other.value
        if not MIN_VAL <= result <= MAX_VAL:
            result %= MIN_VAL * -2
        return JavaLong(result)
    
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return int(self.value)

def convert(strInput):
    j2 = JavaLong(0)
    for i in range(len(strInput)):
        j2 = (j2 * JavaLong(31)) + JavaLong(ord(strInput[i]))
        print(j2)
