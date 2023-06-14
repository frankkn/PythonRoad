def calculate(a, operator, b):
    try:
        a = int(a)
        b = int(b)
        if operator == "+":
            print("{:.2f}".format(a+b))
        elif operator == "-":
            print("{:.2f}".format(a-b))
        elif operator == "*":
            print("{:.2f}".format(a*b))
        else: # operator == "/"
            try:
                print("{:.2f}".format(a/b))
            except ZeroDivisionError:
                print("Can divided by 0.")

    except ValueError:
        print("Integers only.")