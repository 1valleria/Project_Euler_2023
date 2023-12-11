## Question 1
#def sum_of_multiples(limit):
#    result = 0
#    for i in range(limit):
#        if i % 3 == 0 or i % 5 == 0:
#            result += i
#    return result

#limit = 1000

#result = sum_of_multiples(limit)
#print(f"The sum of multiples of 3 or 5 below {limit} is: {result}")

# Question 2
#def even_fibonacci_sum(limit):
#    a, b = 1, 2
#    even_sum = 0

#    while a <= limit:
#        if a % 2 == 0:
#            even_sum += a

#        a, b = b, a + b

#    return even_sum

#limit = 4000000

# Call the function and print the result
#result = even_fibonacci_sum(limit)
#print(f"The sum of even-valued terms in the Fibonacci sequence below {limit} is: {result}")

#Question 3
#def largest_prime_factor(n):
#    i = 2
#    while i * i <= n:
#        if n % i:
#            i += 1
#        else:
#            n //= i
#    return n

#number = 600851475143
#result = largest_prime_factor(number)
#print("The largest prime factor of", number, "is:", result)

MOD = 10**9 + 7

def calculate_Rk(N, k):
    dp = [[0] * (k + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        dp[i][0] = 1

    for i in range(1, N + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i - 1][j] * (j + 1) + dp[i - 1][j - 1]) % MOD

    result = 0
    for i in range(1, k + 1):
        result = (result + dp[N][i]) % MOD

    return result

N = 10000
k = 6
result = calculate_Rk(N, k)
print(result)
