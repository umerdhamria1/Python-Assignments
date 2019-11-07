import sys
import datetime
import math

#Q1
print('Twinkle, twinkle, little star,');
print ('     How I wonder what you are!');
print('            Up above the world so high,');
print('            Like a diamond in the sky.') ;
print('Twinkle, twinkle, little star,');
print('      How I wonder what you are');

#Q@
print('Python Version is : ' + sys.version)

#Q3
today = str(datetime.datetime.now())
print('Date and time is: ' + today)

#Q4
r=float(input('Input the radius of the circle : '))
print ('The Area of the circle with radius '+ str(r)+' is: '+ str(math.pi * r **2))

#Q5
FirstName=str(input('Enter your First Name: '))
LastName=str(input('Enter your Last Name : '))
FullName = FirstName+ ' ' + LastName [::-1]
print (FullName)

#Q6
Param1=int(input('Enter First Value :'))
Param2=int(input('Enter Second Value :'))
Total = Param1 + Param2
print('Total :' + str(Total))


