# encoding:utf-8
def division(dividend, divisor):
    """perform arithmetric division"""
    try:
        return dividend/divisor
    except ZeroDivisionError:
        # raise ZeroDivisionError("Please provide greater than 0 value*************")
        # return None
        return "Please provide greater than 0 value*"

res = division(9,0)
print(res)