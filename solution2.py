# Write code for algorithm 2 below
def count(num, x=1):
    if x > num:
        return
    else:
        print(x)
        count(num, x + 1)


count(3)
