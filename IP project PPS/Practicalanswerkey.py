                        # Practical IP    SET A
"""i)Write the code to create a dataframe’df’ and answer  the question followed.
Name	Math	IP	English
Puneet	100	99	96
Prajwal	84	90	75
Abhishek97	100	94"""

import pandas as pd
data={'Maths':{'Puneet':100,'Prajwal':84,'Abhishek':97},
     'IP':{'Puneet':99,'Prajwal':90,'Abhishek':100},
     'English':{'Puneet':96,'Prajwal':75,'Abhishek':94}
     }
df=pd.DataFrame(data)
print(df)
#i)a)	Write a command to add one column Total=Math+IP+English
      

df['Total']=df['Maths']+df['IP']+df['English']
print(df)

#b)      Write a command to add one row Raju with values 75.6,87.5,66
df.loc['Raju', :] = [75, 83, 89,247]
print(df)
#c)	Write a command to print Score of Math and IP only.
df=df[['Maths','IP']]
print(df)
#d)	Write a command to update marks in IP of Abhishek  85

df.at['Abhishek','IP']=85
print(df)
#e)	Write a command to delete a row Prajwal.

df=df.drop('Raju')
print(df)

"""Write a python program to display the given  Result using  a bar chart (table is given in Q1.(A)
(i)	Set the title of graph is “Result Analysis”
(ii)	Display the legends.
(iii)	Display the label of x axis to Name” and y axis  to “score"""

import numpy as np
import matplotlib.pyplot as plt

subject = ['Maths', 'IP', 'Eng']

Puneet = [90, 85, 92.5]
Abhishek= [95, 100.0, 57.48]
Prajwal= [85, 100.0, 53.58]
x_axis = np.arange(len(subject))
plt.bar(x_axis - 0.25, Puneet, 0.25, label='Puneet')
plt.bar(x_axis, Abhishek, 0.25, label='Abhishek')
plt.bar(x_axis + 0.25, Prajwal, 0.25, label='Prajwal')
plt.xticks(x_axis,subject)
plt.legend(loc=1)
# Adding titles and labels

plt.xlabel("Name")
plt.ylabel("Score")
plt.title("Result Analysis")
plt.show()
#_________________________________________________________________________________________________________________________________________________________

                         #SET-B
#1.	Write a program to generate a series using a dictionary to represent month number and month names.
import pandas as pd
def Ser_dic():
    di = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
          7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    s = pd.Series(di)
    print(s)
Ser_dic()
#b) Write a program to generate a series of marks of 10 students. Give grace marks up to 5 of those who are having <33 marks and print the new list of the marks.
import pandas as pd
def Ser_stumarks():
    std_marks = []
    for i in range(1,11):
        m = int(input("Enter the marks:"))
        std_marks.append(m)
    s = pd.Series(index=range(1201,1211),data=std_marks)
    s[s<33]=s+5
    print("New List is:")
    print(s[s>=33])
Ser_stumarks()
#2.Consider the table
#1.	Create a dataframe using lists.
#2.	Display books for class XII.
#3.	Display the books whose price is more than 250.
#4.	Plot these data on line chart.

import pandas as pd
import matplotlib.pyplot as mpp
#Answer 1
data={'BookID':['B0001','B0002','B0003','B0004','B0005','B0006'],\
      'Subject':['Computer Science','Computer Science','Computer Appllications',\
      'Informatics Practices','Artificial Intelligence','Informatics Practices'],\
      'Class':['XII','XII','X','XII','IX','XII'],\
      'Publisher':['NCERT','Dhanpat Rai','BPB','NCERT','KIPS','Oswal books'],\
      'Price':[270,340,120,270,340,299]}
books=pd.DataFrame(data)
#Asnwer 2
print("Class XII Books:")
print(books[books['Class']=='XII'].to_string(header=False,index=False))
print("***********************************************************")
#Asnwer 3
print("Books having price more than 250")
print(books[books['Price']>250].to_string(header=False,index=False))
#Answer 4
books.plot(x='Subject',y='Price',kind='line')
mpp.show()
#_____________________________________________________________________________________________________________________
 #                                                               Set-C

import pandas as pd 
Cr_No=[1,2,3,4]
Name=['Arnesh Gupta','Aditya Tiwari','Sakhsham De','Aryan Kunwar']
Score1=[92,65,70,80]
Score2=[83,45,91,75]
data={'Cr_No':Cr_No,'Name':Name,'Score1':Score1,'Score2':Score2}
crickter=pd.DataFrame(data)
print(crickter)
#ii) Dispaly the highest score in both Score1 and Score2 of the Dataframe
print("\n\n#ii. Display the highest score in both Score1 and Score2 of the Dataframe\n\n")
print("Highest of Score1:",crickter['Score1'].max())
print("Highest of Score2:",crickter['Score2'].max())

#iii) Display the Daaframe.
print("\n\n#iii. Display the DataFrame\n\n")
print(crickter)
#iv) Display the details of Sakhsham De
print("\n\n#iv. Display the details of Sakhsham De\n\n")
print(crickter[crickter['Name']=='Sakhsham De'])

import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame using lists
data = {
    'BookID': ['B0001', 'B0002', 'B0003', 'B0004', 'B0005', 'B0006'],
    'Subject': ['Computer Science', 'Computer Science', 'Computer Applications', 'Informatics Practices', 'Artificial Intelligence', 'Informatics Practices'],
    'BookTitle': ['NCERT Computer Science', 'Move fast with computer science', 'Sample Papers', 'NCERT Computer Science', 'Artificial Intelligence', 'CBSE Questions Bank'],
    'Class': ['XII', 'XII', 'X', 'XII', 'IX', 'XII'],
    'Publisher': ['NCERT', 'Dhanpat Rai', 'BPB', 'NCERT', 'KIPS', 'Oswal Books'],
    'Price': [270, 340, 120, 270, 340, 299]
}

df = pd.DataFrame(data)
print(df)

# Display books for class XII
class_XII_books = df[df['Class'] == 'XII']
print("Books for Class XII:\n", class_XII_books)

# Display the books whose price is more than 250
expensive_books = df[df['Price'] > 250]
print("\nExpensive Books:\n", expensive_books)

# Plotting data on a pie chart
class_distribution = df['Class'].value_counts()
plt.pie(class_distribution, labels=class_distribution.index, autopct='%1.1f%%', startangle=90)
plt.title('Class Distribution of Books')
plt.show()



