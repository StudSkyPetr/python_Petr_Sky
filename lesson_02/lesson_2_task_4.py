def fizz_buzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
                print("Fizz")
        elif (i % 5 == 0):
                print("Buzz")
        else:    print(i)

nom = int(input("Вводите количество цыфр для запуска процесса проверки   "))
nnn = fizz_buzz(nom)
