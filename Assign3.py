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
Customer = {"FirstName":"Ali",
           "LastName":"Abdul Razzaq",
           "Mobile":"0322",
           "FirstName":"Ahmed",
           "LastName":"Ali",
           "Mobile":"0333",
           "FirstName":"Yasir",
           "LastName":"Aziz",
           "Mobile":"0321"}
print(Customer["FirstName"])
#PROBLEM 4
Total =[]
Customer = {"FirstName":"Ali",
           "LastName":"Abdul Razzaq",
           "Amount":"10",
           "FirstName":"Ahmed",
           "LastName":"Ali",
           "Amount":"10",
           "FirstName":"Yasir",
           "LastName":"Aziz",
           "Amount":"10"}
for num in Customer["Amount"].Value:
     ##Total.append(num)
     print(str(num))

#PROBLEM 5