a = int(input("a값"))
b = int(input("b값"))

def multi_recur(a, b):
    if b == 1:
        return a
    else:
        return a + multi_recur(a, b-1)
print(multi_recur(a, b))