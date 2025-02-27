def algorithm(n):
    j = 0
    for i in range(n):
        while j >= 1:
            j -= 1

        j += 1
    return j

n = 10
print(algorithm(n))
