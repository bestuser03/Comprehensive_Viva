# take a n number and computes n+nn+nnn

number = int(input("Enter a number n: "))

temp = str(number)

t1 = temp + temp
t2 = temp + temp + temp

num = number + int(t1) + int(t2)

print(f"The value is:{num}")