# encoding:utf-8
import math


def is_prime(num):
    prime = True
    # 如果输入数字没有大于它自己平方根的因数，那么它就一定是一个素数
    for item in range(2, int(math.sqrt(num)) + 1):
        if num % item == 0:
            prime = False
    return prime


def get_prime_numbers(lower, higher):
    for possible_prime in range(lower, higher):
        if is_prime(possible_prime):
            yield possible_prime
        yield False


for _prime in get_prime_numbers(lower=1, higher=100):
    if _prime:
        print(_prime)

