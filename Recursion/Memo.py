#For memoization, we use hash tables

def fib(n, memo):
    #our function accepts two parameters
    if n == 0 or n == 1: #base case
        return n 
    if not memo.get(n):
    #if n is NOT in memo, compute fib(n) with recursion
    #and then store the result in a hash table
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    # By now , fib(n)'s result is certainly in memo. This is where we store the result of the 
    # calculation in memo into the has table
    return memo[n]

print(fib(100,{}))


    