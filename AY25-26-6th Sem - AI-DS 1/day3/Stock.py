# stock analysis

def analysis(history):
    if len(history)<2:
        print("Invalid history")
        return
    current_buy = history[0]
    current_sell = history[1]
    max_profit = current_sell - current_buy
    
    for today in history[1:]:
        temporary_profit = today - current_buy
        # check for new max profit, to change sell
        if temporary_profit>max_profit:
            max_profit = temporary_profit
            current_sell = today
        # check for new min buy
        if today < current_buy:
            current_buy = today
    print((current_sell-max_profit), current_sell)
    return
    

analysis([45, 12, 3, 10, 50])
analysis([-10, -5, -2, -1, 1])
analysis([90, 40, 20, 10, 4])