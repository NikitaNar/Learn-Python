def rec(a):
    if a==0:
        return a
    else:
        return a+rec(a-1)
print(rec(5))