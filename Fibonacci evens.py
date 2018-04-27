
def fibonacci(n):
    # function returns the fibonacci sequence up to n
    fib_seq = [1]
    n1 = 1
    n2 = 1
    for i in range(n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if n3 > n:
            break
        fib_seq.append(n3)
    result = 0
    for i in fib_seq:
        if i % 2 == 0:
            result += i
    return result

user_input = input("This programme takes a number and returns \n the sum of every even term in the fibonacci sequence up to that number. \n Please enter a number:")
answer = fibonacci(int(user_input))
print("Answer: %d" % (answer))
