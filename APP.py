print("Hello World")
TEST1="FIRST"
TEST2="second"
print("--Test of variables:")
print("Test1:" + TEST1)
print("Test2:" + TEST2)
print("drop row\ndroped\n\n\n\n")
print("\"add quataions\"")
num1=-10
print("number:" + str(num1) + "\nabsolute:" + str(abs(num1)))
name = input("Enter your name please:")
print("Hello "+ name)
num2 = input("enter first number: ")
num3 = input("enter second number: ")
sum = float(num2) + int(num3)
print(sum)
array1 = ["shay", "mor", "dima", "moria", "toot"]
print("The first name is:" + array1[0])
print("the last name is: " + array1[-1])
print("the 3rd one: " + array1[3])
array1[4] = input("insert a new name insted of " + array1[4])
print("new name: " + array1[4])
array2 = [1, 3, 2, 6, 0, 9]
array1.extend(array2)
array1.append("dov")
print(array1)
array1.insert(3, "book")
print(array1)
array1.remove("book")
print(array1)
array1.remove(3)
print(array1)
print(array1.index(2))
print(array1.index("mor"))


def sayhi():
    print("hi")
    print("hihi")

sayhi()

def print_multi_hi(numofhi):
    return numofhi*100

print(print_multi_hi(3))

test1 = input("insert number to check: ")
if int(test1)>10 and True:
    print("bigger")
elif int(test1)>5:
    print("wired")
else:
    print("smaller")

print("\n\n\n")
i=1
while i<=10:
    print(i)
    i += 1

print("done while loop")

print("\n\n")

for index in array1:
    print(index)

print("\n\n\nnumber grid:")
num4 = [
    [0,2,4,6],
    [1],
    [3,5,7],
    [8,10,12,14,16,18,20],
    [9,11,13,15],
    [17,19]
]
for index in num4:
    print(index)

print ("\n\n")
for index in num4:
    for index2 in index:
        print(index2)

#This is a cooment

try:
    num1 = int(input("Enter a whole number please: "))
    print(num1)
except ValueError:
    print("invalid input")

try:
    file1 = open("test1.txt", "r")
    linenum = 1
    for row in file1.readlines():
        #print(row + " row number: " + index(row))
        print(row + " row number: " + str(linenum))
        linenum += 1
    file1.close()
except:
    print("file is not accessible")