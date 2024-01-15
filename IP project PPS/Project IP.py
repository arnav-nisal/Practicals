import pandas as pd
import matplotlib.pyplot as plt


def main_menu():
    print("\n------- Student Management System -------\n")
    print("1. Create/Import New Dataframe")
    print("2. Student Data Analysis")
    
    print("3. Student Data Visualisation")
    print("4. Export Dataframe to csv file")


def create_dataframe_menu():
    print("\n------- Create Dataframe -------\n")
    print("1. Create Dataframe")
    print("2. Import Dataframe from csv file")
    print("3. Add/Modify Custom Index")
    print("4. Add/Modify Custom Column Head")
    print("5. Return to main menu")


def analysis_menu():
    print("\n------- Data Analysis using Python -------\n")
    print("1.  Display All records")
    print("2.  Print first nth records")
    print("3.  Print last nth records")
    print("4.  Print All records in order of Name")
    print("5.  Display student with maximum marks")
    print("6.  Display student with minimum marks")
    print("7.  Display students who have secured passing marks")
    print("8.  Print distinct classes")
    print("9.  Add a row to Dataframe")
    print("10. Delete a row from Dataframe")
    print("11. Return to main menu")


def visualisation_menu():
    print("\n------- Visualisation using Matplotlib -------\n")
    print("1. Plot Line graph (Subject wise marks)")
    print("2. Plot Bar graph (Students, Marks)")
    print("3. Plot Horizontal Bar graph (Student, Class)")
    print("4. Return to main menu")


cols = ['admn', 'name', 'dob', 'class', 'maths', 'english', 'science', 'marks']
df = pd.DataFrame([], columns=cols)  # Create an EmptyDataFrame
while True:
    main_menu()
    ch = int(input("Select Option: "))
    if ch == 1:
        # Create New Dataframe
        create_dataframe_menu()
        ch = int(input("Select Option: "))
        if ch == 1:
            data = []
            while True:
                ch = input("Add Row [y/n]")
                if ch.lower() == 'y':
                    admn = int(input("Admission Number: "))
                    name = input("Student Name: ")
                    dob = input("DOB in dd-mm-yyyy format: ")
                    std = int(input("Class: "))
                    maths = float(input("Maths: "))
                    english = float(input("English: "))
                    science = float(input("Science: "))
                    marks = maths + english + science
                    data.append([admn, name, dob, std, maths, english, science, marks])
                else:
                    break
            df = pd.DataFrame(data, columns=cols)
        elif ch == 2:

            file = input("C:\\users\\arnav\\PycharmProjects\\pythonProject\\IP project PPS\\Book2.csv")

            df = pd.read_csv("C:\\users\\arnav\\PycharmProjects\\pythonProject\\IP project PPS\\Book2.csv")
        elif ch == 3:
            index_list = input("Index List: ").split(",")
            df.index = index_list
        elif ch == 4:
            column_list = input("Column List: ").split(",")
            df.columns = column_list
        print(df)

    elif ch == 2:
        while True:
            # Student  Data Analysis
            analysis_menu()
            ch = int(input("Select Option: "))
            if ch == 1:
                print(df)
            elif ch == 2:
                nth = int(input("Enter no of rows to display: "))
                print(df.head(nth))
            elif ch == 3:
                nth = int(input("Enter number of rows to display: "))
                print(df.tail(nth))
            elif ch == 4:
                print(df.sort_values(by='name'))
            elif ch == 5:
                print(df[df['marks'] == df['marks'].max()])
            elif ch == 6:
                print(df[df.marks == df["marks"].min()])
            elif ch == 7:
                print(df[df['marks'] * 100 / 240 >= 33])
            elif ch == 8:
                print(df['class'].unique())
            elif ch == 9:
                while True:
                    ch = input("Add Row [y/n]")
                    if ch.lower() == 'y':
                        admn = int(input("Admission Number: "))
                        name = input("Student Name: ")
                        dob = input("DOB in dd-mm-yyyy format: ")
                        std = int(input("Class: "))
                        maths = float(input("Maths: "))
                        english = float(input("English: "))
                        science = float(input("Science: "))
                        marks = maths + english + science
                        df = df.append({"admn": admn, "name": name,
                                        "dob": dob, "class": std, "maths": maths,
                                        "english": english, "science": science,
                                        "marks": marks}, ignore_index=True)
                    else:
                        break
            elif ch == 10:
                print("1. Delete Row by Index")
                print("2. Delete Row by Admn No.")
                ch = int(input("Select Option: "))
                if ch == 1:
                    idx = int(input("Index to delete: "))
                    df = df.drop(index=idx)
                elif ch == 2:
                    admn = int(input("Admn no to delete: "))
                    df = df.drop(df[df["admn"] == admn].index)
                else:
                    print("Wrong Option Selected! ")
            else:
                print("Returning to main menu")
                break
    elif ch == 3:
        while True:
            # Student Data Visualisation
            visualisation_menu()
            df = pd.read_csv("C:\\users\\arnav\\PycharmProjects\\pythonProject\\IP project PPS\\Book2.csv")
            ch = int(input("Select Option: "))
            if ch == 1:
                plt.plot(df['name'], df['maths'], label='Maths', color="blue", marker="*")
                plt.plot(df['name'], df['english'], label='English', color="green", marker="*")
                plt.plot(df['name'], df['science'], label='Science', color="purple", marker="*")
                plt.xlabel("Student", fontsize=12)
                plt.ylabel("Marks", fontsize=12)
                plt.title("Subject Wise Marks of Students", fontsize=16)
                plt.legend()
                plt.show()
            elif ch == 2:
                x_values = df["name"]
                y_values = df['marks']
                plt.bar(x_values, y_values, color='orange')
                plt.xlabel("Students", fontsize=12)
                plt.ylabel("Marks", fontsize=12)
                plt.title("Students - Marks Visualisation", fontsize=14)
                plt.show()
            elif ch == 3:
                x_values = df["name"]
                y_values = df["class"]
                plt.barh(x_values, y_values, color='magenta')
                plt.xlabel("Students", fontsize=12)
                plt.ylabel("Class", fontsize=12)
                plt.title("Students - Class Visualisation", fontsize=16)
                plt.show()
            elif ch == 4:
                print("Returning to main menu")
                break
            else:
                print("Wrong Option Selected! ")
    elif ch == 4:
        # Export Dataframe to csv file
        # file = input("C:\\users\\arnav\\PycharmProjects\\pythonProject\\Book2.csv")
        file = 'C:\\users\\arnav\\PycharmProjects\\pythonProject\\Book2.csv'
        df.to_csv(file, index=False)
    elif ch == 5:
        # Exit
        print("Bye ...")
        exit()
    else:
        # Error Display and Exit
        print("Error! Wrong option selected. ")
