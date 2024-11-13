i = 1

while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i * j}", end=" | ")
        j += 1
    i += 1
    print("\n")