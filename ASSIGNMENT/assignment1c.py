#First, we will take the input:
lower_value=int(input("Please ,Enter the Lowest Range value: "))
upper_value=int(input("Please, Enter the Upper Range value: "))
print("The Prime Numbers in the range are: ")
for number in range(lower_value,upper_value +1):
        if number>1:
            for i in range(2,number):
                if(number%i) == 0:
                    break
                else:
                    print(number)
                    