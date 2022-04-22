numbers = list(range(1,10))
for n in numbers:
    if n == 1:
        print(f"{n}st", end=' ')
    elif n == 2:
        print(f"{n}nd", end=' ')
    elif n == 3:
        print(f"{n}rd", end=' ')
    else:
        print(f"{n}th", end=' ')
print()