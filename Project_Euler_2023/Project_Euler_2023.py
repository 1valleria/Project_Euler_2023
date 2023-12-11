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

# #Question 2
#def even_fibonacci_sum(limit):
#    a, b = 1, 2
#    even_sum = 0

#    while a <= limit:
#        if a % 2 == 0:
#            even_sum += a

#        a, b = b, a + b

#    return even_sum

#limit = 4000000

# #Call the function and print the result
#result = even_fibonacci_sum(limit)
#print(f"The sum of even-valued terms in the Fibonacci sequence below {limit} is: {result}")

##Question 3
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
##Question 4

def is_palindrome(n):
    # Convert the number to a string and check if it reads the same backward and forward
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

result = largest_palindrome_product()
print("The largest palindrome made from the product of two 3-digit numbers is:", result)
        
