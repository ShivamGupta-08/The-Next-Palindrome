print("Welcome to - The Next Palindrome")
try:
    test_cases = int(input("Enter the number of test cases you want\n"))
    list_of_numbers =[]
    for n in range(test_cases):
        time = int(input("Enter your number\n"))
        list_of_numbers.append(time)

    for i in list_of_numbers:
        x = int(i)
        while True:
            x = str(x)
            if x[::-1] == x :
                print(f"Next palindrome for {i} is {x[::-1]}")
                break
            else:
                x = int(x)
                x += 1
except  ValueError as e:
    print("Please enter only integers. ",e)
