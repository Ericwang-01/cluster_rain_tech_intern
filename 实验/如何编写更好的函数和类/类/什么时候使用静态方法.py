# encoding:utf-8
"""
静态方法与类相关，但不需要访问类的数据，在不依赖类的状态的状态下工作
为什不定义成一个单独的函数呢？静态方法与类相关，放在类里面有利于理解
"""


class BookPriceCalculator:
    PER_PAGE_PRICE = 8

    def __init__(self, pages, author):
        self.pages = pages
        self.auther = author

    @property
    def standard_price(self):
        return self.pages * BookPriceCalculator.PER_PAGE_PRICE

    @staticmethod
    def price_to_book_ratio(market_price_per_share, book_value_per_share):
        return market_price_per_share/book_value_per_share

instance = BookPriceCalculator(100, 'wang')
instance.PER_PAGE_PRICE = 7

print(BookPriceCalculator.PER_PAGE_PRICE)
print(instance.PER_PAGE_PRICE)
my_obj = BookPriceCalculator(1, 'xioamig')
print(my_obj.PER_PAGE_PRICE)