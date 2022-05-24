import Admin
import Register
import User


class MainPage:

    def main(self):
        while True:
            print("\t\t_________________________________________")
            print("\t\t\t -------Main Screen-------")
            print("\t\t_________________________________________")
            print("\t\t\t1-> Admin")
            print("\t\t\t2-> Resgister new user")
            print("\t\t\t3-> User login")
            print("\t\t\t4-> Exit")
            choice = eval(input("\t\t\tEnter your choice(1/2/3/4):- "))
            if choice == 1:
                am = Admin.Admin()
                am.adminscreen()

            elif choice == 2:
                rg = Register.Register();
                rg.register_user()

            elif choice == 3:
                us = User.User()
                us.user_login()

            elif choice == 4:
                exit()

            else:
                print("Invalid input")


mn = MainPage()
mn.main()
