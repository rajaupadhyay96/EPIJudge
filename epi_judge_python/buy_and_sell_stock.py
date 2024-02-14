from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    res = 0
    minSoFar = float("inf")

    for price in prices:
        res = max(res, price-minSoFar)
        minSoFar = min(price, minSoFar)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
