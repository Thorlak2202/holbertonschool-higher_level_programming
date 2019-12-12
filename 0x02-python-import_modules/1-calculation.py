#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as operator
a = 10
b = 5
print("{:d} + {:d} = {:d}".format(a, b, operator.add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, operator.sub(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, operator.mul(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, operator.div(a, b)))
