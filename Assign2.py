#PROBLEM 1
print('-----------------------------')
print('-----------------------------')
print('PROBLEM 1')
Eng = int(input("Enter  English Marks:"))
Urd = int(input("Enter  Urdu Marks:"))
MAT = int(input("Enter  MATH Marks:"))
SCN = int(input("Enter  SCIENCE Marks:"))
CMC = int(input("Enter  CHEMISTRY Marks:"))
Total = int(Eng) +int(Urd) +int(MAT) +int(SCN)+int(CMC)
print('-----------------------------')
print('Marks Obtain Total:',Total,' Out of 500.')

perc= Total * 100 / 500

print ('perc: ',perc,'%')
if perc > 80:
    grade = 'A+1'
elif perc < 80 and perc > 70:
    grade = 'A'
elif perc < 70 and perc > 60:    
    grade = 'B'
elif perc < 60 and perc > 50:    
    grade = 'C'
else: 
    grade = 'D'
print('Grade:',grade)

#PROBLEM 2
print('-----------------------------')
print('-----------------------------')
print('PROBLEM 2')
Num = int(input("Enter a Number to check even or odd: "))
if Num %2 == 0:
    print('Given number is Even:',Num)
else:
    print('Given number is ODD:',Num)


#PROBLEM 3
print('-----------------------------')
print('-----------------------------')
print('PROBLEM 3')
arr = [1,2,3]
a=len(arr)
print('List lenght is :',a)


#PROBLEM 4
print('-----------------------------')
print('-----------------------------')
print('PROBLEM 4')
arr = [1,2,3]
a=sum(arr)
print('Sum of list is :',a)


#PROBLEM 5
print('-----------------------------')
print('-----------------------------')
print('PROBLEM 5')
arr = [1,2,3]
a=max(arr)
print('Max value in list is :',a)

#PROBLEM 6
print('-----------------------------')
print('-----------------------------')
print('PROBLEM 6')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
select_num =[]
for x in a:
    if(x <5):
        select_num.append(x)
    
print('Less than 5 in list are :',select_num)