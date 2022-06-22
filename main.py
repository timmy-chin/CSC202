import time



def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    current = previous = None

    for i in range(n + 1):
        if i == 0:
            current = 0
        elif i == 1:
            previous = current
            current = 1
        else:
            temp = previous
            previous = current
            current = current + temp

    return current

start_time = time.time()
fibonacci(1000000)
end_time = time.time()
print(f'Run Time is for linear: {-1*(start_time - end_time)}')

start_time = time.time()
recursive_fibonacci(1000000)
end_time = time.time()
print(f'Run Time is for recursive: {-1*(start_time - end_time)}')