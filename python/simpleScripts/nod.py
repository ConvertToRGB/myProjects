number = float(raw_input("enter number: "))
numbers = []
n = 2
while number > 1:
    if number % n == 0:
        number = number/n
        numbers.append(n)
        print numbers
    elif number % n != 0:
        n += 1
        if number % n == 0:
            number = number/n
            numbers.append(n)
            print numbers
        elif number % n != 0:
            n += 2
            if number % n == 0:
                number = number/n
                numbers.append(n)
                print numbers
            elif number % n != 0:
                n += 2
                if number % n == 0:
                    number = number/n
                    numbers.append(n)
                    print numbers
