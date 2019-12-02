#PROBLEM 1
First = int(input("Enter  First Value: "))
Second = int(input("Enter  Second  Value: "))
Operator = input("Enter  Operator: ")

if Operator == "+":
    Answer = First + Second
    print('Answer is ',Answer)
elif Operator == "-":
    Answer = First - Second
    print('Answer is ',Answer)
elif Operator == "*":
    Answer = First * Second
    print('Answer is ',Answer)
elif Operator == "/":
    Answer = First / Second
    print('Answer is ',Answer)
else:
    print('Invalid Operator provided')

#PROBLEM 2
List = ["A","B","1","C","'D","8","2","X","Y","Z"]
NumFound = []
for num in List:
    if num.isdigit() ==True:
        NumFound.append(num)    
print('These numbers are found in List: ',NumFound)

#PROBLEM 3
#PROBLEM 4
#PROBLEM 5