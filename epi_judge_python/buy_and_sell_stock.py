from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    n = len(prices)
   
    max_profit = 0
    current_profit = 0
    current_min = prices[0]
    for i in range(1,n):
        if prices[i] < current_min:
            current_min = prices[i]
            current_profit = 0
        else:
            current_profit += prices[i] - prices[i-1]
        max_profit = max(max_profit, current_profit)
    return max_profit

    # current_min = prices[0]
    # max_profit = 0
    # for i in range(1,n):
    #     if prices[i] < current_min:
    #         current_min = prices[i]
    #     else:
    #         profit = prices[i] - current_min
    #         if max_profit < profit:
    #             max_profit = profit
    # return max_profit

    # if n<=1:
    #     return 0 
    # first = prices[:n//2]
    # second = prices[n//2:]
    # return max(buy_and_sell_stock_once(first), buy_and_sell_stock_once(second), max(second) -
    #         min(first))

    # n = len(prices)
    # max_profit = 0
    # buy = 0
    # sell = 0
    # while (buy < n and sell < n):
    #     while (buy < n-1 and prices[buy + 1] <= prices[buy]):
    #         buy +=1
    #     sell = buy-1
    #     while (sell < n-1 and prices[sell +1]>=prices[sell]):
    #         sell +=1
    #     profit = prices[sell-1] - prices[buy-1]
    #     max_profit = max(max_profit, profit)
    #     buy +=1
    # return max_profit

    # for i in range(n-1):
    #     for j in range(i+1, n):
    #         profit = prices[j] - prices[i]
    #         if profit > max_profit:
    #             max_profit = profit
    # return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
