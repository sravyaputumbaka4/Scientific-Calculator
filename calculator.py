import math

class ScientificCalculator:


    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


    def power(self, a, b):
        return math.pow(a, b)

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take sqrt of negative number")
        return math.sqrt(a)


    def log(self, a, base=10):
        if a <= 0:
            raise ValueError("Log undefined for non-positive numbers")
        return math.log(a, base)

    def natural_log(self, a):
        if a <= 0:
            raise ValueError("Ln undefined for non-positive numbers")
        return math.log(a)


    def factorial(self, a):
        if a < 0:
            raise ValueError("Factorial undefined for negative numbers")
        return math.factorial(int(a))


    def sin(self, angle, degree=True):
        if degree:
            angle = math.radians(angle)
        return math.sin(angle)

    def cos(self, angle, degree=True):
        if degree:
            angle = math.radians(angle)
        return math.cos(angle)

    def tan(self, angle, degree=True):
        if degree:
            angle = math.radians(angle)
        return math.tan(angle)


    def asin(self, value):
        return math.degrees(math.asin(value))

    def acos(self, value):
        return math.degrees(math.acos(value))

    def atan(self, value):
        return math.degrees(math.atan(value))


    def sinh(self, a):
        return math.sinh(a)

    def cosh(self, a):
        return math.cosh(a)

    def tanh(self, a):
        return math.tanh(a)


    def pi(self):
        return math.pi

    def e(self):
        return math.e


    def evaluate_expression(self, expression):
        allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
        allowed_names["abs"] = abs
        return eval(expression, {"__builtins__": None}, allowed_names)


if __name__ == "__main__":
    calc = ScientificCalculator()
    print("Scientific Calculator Ready!")
    print("Example: sin(30) =", calc.sin(30))
