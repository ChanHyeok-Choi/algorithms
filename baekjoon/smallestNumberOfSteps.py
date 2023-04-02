import math

def min_steps(x, y):
    n = y - x
    arr = []
    top = math.floor(math.sqrt(n))
    while(n > 0):
        if n - top**2 >= top:
            q = (n - top**2)//top
            for i in range(0, q + 1):
                arr.append(top)
                n -= top
            top -= 1
        else:
            arr.append(top)
            n -= top
            top -= 1

    return len(arr)


for i in range(3, 30):
    x = 0
    y = i
    print('Step ', i, ': ', min_steps(x, y))