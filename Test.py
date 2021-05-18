'''#Q1. Write a python program to print triangle given below. Where user enters the height of triangle.
num = int(input("Enter The Height of the Triangle:"))
n = num  #its for space 
for i in range(0,num):
    for j in range(0,num - i -1):
        print(end=" ")
    #n = n - 2 # decerement
    for j in range(0,i+1):
        print(" * ", end="")
    print("\r")
    
#Q.2 Write a python program to read a file and display no. of consonants, vowels, number, special character and white spaces from file content on screen.
content = input("Enter The Contents:"'\n')
vowels = 0
consonants = 0
number = 0
specialcharacter = 0
whitespaces = 0
content = content.lower()
for i in range(0,len(content)):
    if (content[i] == 'a' or content[i] == 'e' or content[i] == 'i' or content[i] == 'o' or content[i] == 'u'):
        vowels = vowels + 1
    elif ((content[i] >= 'a' and content[i] <= 'z')):
        consonants = consonants + 1
    elif (content[i] >='0' and content[i] <= '9'):
        number = number + 1
    elif (content[i] == ' '):
        whitespaces = whitespaces + 1
    else:
        specialcharacter = specialcharacter + 1
print("Vowels:",vowels)
print("consonants:",consonants)
print("number:",number)
print("specialcharacter",specialcharacter)
print("whitspaces:",whitespaces)

# Q.3 Write a python program to determine whether a given number is Even or Odd Recursively.
#1st solution
def num(a):
  if a < 2:
        return (a % 2 ) == 0
  return (a - 2)
a = int(input("Enter The Number:"))
if (num(a)== True):
    print("It is a Even Number")
else:
    print("It is an Odd Number")
 #2nd solution   
number = int(input("ENter the Number:"))
if (number % 2) == 0:
    print("It is Even")
else:
    print("It is Odd")
    
# Q. 4 Write a python program to Multiply all the items in a Dictionary
my_dict = {'A':10,'B':10,'C':237}
result = 1
for key in my_dict:
    result = result * my_dict[key]
print(result)

# Q .5 Write a python program to create a Class which performs basic calculator operations
class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Add(self):
        return self.a + self.b
    def Sub(self):
        return self.a - self.b
    def Mult(self):
        return self.a * self.b
    def Div(self):
        return self.a / self.b
    
n = int(input("Enter The First Number:"))
m = int(input("Enter The Second Number:"))
cal = calculator(n,m)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Divison")

    choice = int(input("ENter Your Choice:"))
    if choice == 1:
        print("result:",cal.Add())
    elif choice == 2:
        print("result:",cal.Sub())
    elif choice == 3:
        print("result:",cal.Mult())
    elif choice == 4:
        print("result:",cal.Div())
    elif choice == 0:
        print("Exit")
    else:
        print("Invalid Choice")'''
    
def user():
    for i in range(1,20,2):
        return i
print(user())
