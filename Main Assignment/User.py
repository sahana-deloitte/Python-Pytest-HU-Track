from openpyxl import *
import Register
import Admin as ad


class User:
    title = ""
    showTiming = 0
    no_of_seats = 0
    email = ""
    password = ""
    a = ad.Admin()

    def user_login(self):
        file = "userdata.xlsx"
        wb = load_workbook(file)
        ws = wb['Sheet1']
        print("******Welcome to BoyMyShow*******\n")
        self.email = input("enter email:- ")
        self.password = input("enter password:- ")
        final = []
        i = -1
        flag = 0
        for row in ws:
            l = []
            for col in row:
                l.append(col.value)
            final.append(l)
            i += 1
        for k in range(len(final)):
            for j in range(len(final[k])):
                if final[k][j] == self.email and final[k][j + 1] == self.password:
                    flag = 1
                    print("login successfully")
                    print("--------------------------------")
                    print("******Welcome " + self.email + " ******* ")
                    self.select_option()
        if flag == 0:
            print("record not found,please register to continue")
            r = Register.Register()
            r.register_user()

    def select_option(self):
        while True:
            print("1.Book tickets\n2.Cancel Tickets\n3.Give User Rating\n4.exit")
            Userchoice = int(input("enter the choice "))
            if Userchoice == 1:
                self.book_tickets()
            elif Userchoice == 2:
                self.cancel_booking()
            elif Userchoice == 3:
                self.user_rating()
            elif Userchoice == 4:
                return
            else:
                print("invalid input")

    def book_tickets(self):

        for i in range(len(self.a.added_movies)):
            print(self.a.added_movies[i]["title"])
        self.title = input("enter the movie name to be booked:- ")
        for i in range(len(self.a.added_movies)):
            if self.a.added_movies[i]["title"] == self.title:
                print(self.a.added_movies[i])
                print(self.a.movie_timings[self.title])
        le = len(self.a.movie_timings[self.title])

        print("No fo shows " + str(le))
        self.showTiming = int(input("select the show timing "))
        self.showTiming = self.showTiming - 1
        fetch = self.a.movie_timings[self.title][self.showTiming]
        tot_capacity = list(fetch.values())
        seats = tot_capacity[0]

        print("Remaining seats: " + str(seats))
        self.no_of_seats = int(input("Enter no of seats\n "))
        while True:
            if self.no_of_seats > seats:
                print("no of tickets should be less than seating capacity ")
                self.no_of_seats = int(input("Enter no of seats\n "))
            else:
                break
        seats = seats - self.no_of_seats
        update_seats = list(fetch.keys())

        lst = self.a.movie_timings[self.title]
        new_dict = lst[self.showTiming]
        new_dict.update({update_seats[0]: seats})
        lst[self.showTiming] = new_dict
        self.a.movie_timings.update({self.title: lst})
        print("Thanks for booking")
        print(seats)

    def cancel_booking(self):
        print(self.a.movie_timings[self.title])
        le = len(self.a.movie_timings[self.title])
        print("Cancel booking")
        fetch = self.a.movie_timings[self.title][self.showTiming]
        tot_capacity = list(fetch.values())
        seats = tot_capacity[0]
        seats = seats + self.no_of_seats
        update_seats = list(fetch.keys())

        lst = self.a.movie_timings[self.title]
        new_dict = lst[self.showTiming]
        new_dict.update({update_seats[0]: seats})
        lst[self.showTiming] = new_dict
        self.a.movie_timings.update({self.title: lst})
        print("Tickets Cancelled")
        print(self.a.movie_timings[self.title][self.showTiming])

    def user_rating(self):
        for i in range(len(self.a.added_movies)):
            print(self.a.added_movies[i]["title"])
        mov_name = input("enter the movie name to give the rating ")
        for i in range(len(self.a.added_movies)):
            if self.a.added_movies[i]["title"] == mov_name:
                flag = 1
                mov_rating = eval(input("enter your rating out of 10 "))
                break
        if flag == 0:
            print("enter proper movie title from given list ")
        file = "userdata.xlsx"
        wb = load_workbook(file)
        ws = wb['Sheet2']
        li = [self.email, mov_name, mov_rating]
        final = []
        i = -1
        for row in ws:
            l = []
            for col in row:
                l.append(col.value)
            final.append(l)
            i += 1
        final.append(li)
        # print(final)
        ws.insert_rows(i)

        i = 0
        for row in ws:
            j = 0
            for index, col in enumerate(row):
                col.value = final[i][j]
                j += 1
            i += 1
        wb.save("userdata.xlsx")
