

n = int(input("please type a number you want to generate:" ))

count_number = 0

while count_number<n:
    count_number += 1
    if count_number%3==0 and count_number%5 != 0:
        res = "Fizz"
    elif count_number%5 ==0 and count_number%3!=0:
        res = "Buzz"
    elif count_number%3 ==0 and count_number%5 ==0 :
        res = "FizzBuzz"
    else:
        res = count_number
    print(res)
