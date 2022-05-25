from openpyxl import *


class Register:
    def register_user(self):

        print("****Create new Account*****\n")
        name = input("Enter the name\n ")
        email = input("Enter the email\n ")
        password = input("Enter the password\n ")
        phone = int(input("Enter the Phone number\n "))
        age = int(input("Enter the age\n "))
        file = "userdata.xlsx"
        workBook = load_workbook(file)
        workSheet = workBook['Sheet1']

        list = [name, email, password, phone, age]
        result = []
        initial = -1
        for row in workSheet:
            list1 = []
            for col in row:
                list1.append(col.value)
            result.append(list1)
            initial += 1
        result.append(list)
        # print(result)
        workSheet.insert_rows(initial)

        initial = 0
        for row in workSheet:
            jloop = 0
            for index, col in enumerate(row):
                col.value = result[initial][jloop]
                jloop += 1
            initial += 1
        workBook.save("userdata.xlsx")
