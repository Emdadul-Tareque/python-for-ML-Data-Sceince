# number1 = input("Enter First Number: ")
# number2 = input("Enter Second Number: ")
# sum = int(number1) + int(number2)
# print("Total: ", sum)

# try:
#     number1 = int(input("Enter First Number: "))
#     number2 = int(input("Enter Second Number: "))
# except:
#     print("Your input number is not valid")

while True:
    try:
        number1 = int(input("Enter First Number: "))
        number2 = int(input("Enter Second Number: "))
        break
    except:
        print("Your input number is not valid")
    finally:
        sum = number1 + number2
        print(sum)







