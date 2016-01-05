size=input("enter number")
size=int(size)
def pattern(size):
    for i in reversed(range(1, size)):
        print (" " * (size - 1), "*" * i)