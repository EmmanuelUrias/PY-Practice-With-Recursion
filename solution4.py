# Write code for algorithm 4 below

def power(a, b=2):
    if b == 1:
        return a
    else:
        return a * power(a, b - 1)


print(power(2, 4))
