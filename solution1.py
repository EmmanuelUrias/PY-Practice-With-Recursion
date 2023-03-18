# Write code for algorithm 1 below

def print_number_to_zero(num=int):
    if num <= 0:
        return
    else:
        print(num)
        print_number_to_zero(num - 1)


print_number_to_zero(300)
