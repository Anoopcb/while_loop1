##print("Hello world") for 10 times

i = 1

while i <=10:

    print("Hello World")
    i+=1

## sum from 1 to 50 using while loop
total = 0
num = 1

while num <=50:

    total = total + num
    num +=1
print(total)
## program for sum of number from 1 to entered number by while loop
n = input("please enter a number ")
n = int(n)

intotal = 0

nums = 1

while nums <=  n:

    intotal += nums

    nums+=1

print("your total is ", intotal)


number1 = input("please enter your number ")
#int(number1[nums1])+
total1 = 0

nums1 = 0

while nums1 < len(number1):

    total1 += int(number1[nums1])
    nums1+=1
## this is for adding digits in a number
print("Total of you number's digits is ",  total1)


name = input("please enter your name ")

num2 = 0
temp = ""
while num2 < len(name):


    if name[num2] not in temp:
        temp += name[num2]

        print(f"{name[num2]} : {name.count(name[num2])}")

    num2 += 1