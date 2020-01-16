'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
'''

# Solution1:遞歸解法
# 這種遞歸屬於多路徑遞歸,人腦不可能人肉模擬完整的遞和歸過程,只能通過遞歸樹和假設子問題已經得到解決的方式來寫遞推公式
def coinChange(coins, amount):
    def helper(value):
        if value == 0: return 0
        res = float('inf')
        for coin in coins:
            if value - coin < 0: continue
            sub_res = helper(value-coin)
            if sub_res == -1: continue
            res = min(res, helper(value-coin)+1)
        return res if res != float('inf') else -1

    return helper(amount)


# Solution2:加備忘錄的遞歸解法
def coinChange(coins, amount):
    def helper(value):
        if value in d: return d[value]
        if value == 0: return 0
        res = float('inf')
        for coin in coins:
            if value - coin < 0: continue
            sub_res = helper(value-coin)
            if sub_res == -1: continue
            res = min(res, sub_res+1)
        d[value] = res if res != float('inf') else -1
        return d[value]

    d = {}
    return helper(amount)


# Solution3:動態規劃
# 遞歸的解法思路是把大數值一直拆分遞歸到小數值,即要找到遞歸的終止條件
# 動態規劃的解法思路是從小數值開始,推算出大數值的求值規律
def coinChange(coins, amount):
    if not coins or not coins[0]: return -1
    cache = [amount+1] * (amount+1)
    cache[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                cache[i] = min(cache[i], cache[i-coin]+1)    
    return -1 if cache[amount] > amount else cache[amount]


if __name__ == '__main__':
    print(coinChange([408, 186, 83, 419], 6249))
    # print(coinChange([1, 2, 5, 10], 27))