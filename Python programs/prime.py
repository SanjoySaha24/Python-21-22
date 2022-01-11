def primeCheck(num):
    check = 0

    for x in range(2, num):
        if (num % x) == 0:
            check = 1
            break

    if check == 0:
        return True
    else:
        return False