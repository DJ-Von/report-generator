x = int(input("Enter number: "))
first = x//100
second = x//10%10
third = x%10
msg = "Sum is: "
print(msg, first+second+third)
