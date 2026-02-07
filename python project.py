while True:
    print("\n1.Check Result  2.Exit")
    ch = input("Choice: ")

    if ch == "1":
        r = input("Roll No: ")
        m1 = int(input("Sub1: "))
        m2 = int(input("Sub2: "))
        m3 = int(input("Sub3: "))

        total = m1 + m2 + m3
        avg = total / 3

        print("Roll:", r)
        print("Total:", total)
        print("Average:", avg)

        if m1 < 35 or m2 < 35 or m3 < 35:
            print("Result: FAIL")
        else:
            grade = "A" if avg >= 75 else "B" if avg >= 60 else "C" if avg >= 50 else "D"
            print("Result: PASS")
            print("Grade:", grade)

    elif ch == "2":
        break
    else:
        print("Invalid choice")
