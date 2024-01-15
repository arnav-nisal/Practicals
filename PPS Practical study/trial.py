import pandas as pd


def Ser_stumarks():
    std_marks = []
    for i in range(1, 11):
        m = int(input("Enter the marks:"))
        std_marks.append(m)
    s = pd.Series(index=range(1201, 1211), data=std_marks)
    s[s < 33] = s + 5
    print('Entered values:')
    print(std_marks)
    print()
    print("New List is:")
    print(s[s >= 33])


Ser_stumarks()
