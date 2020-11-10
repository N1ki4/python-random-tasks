def fibonacci(num):
    if num < 1:
        return "Wrong input"
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibonacci(num - 2) + fibonacci(num - 1)


print([fibonacci(num) for num in range(15)])
print(fibonacci(-1))
