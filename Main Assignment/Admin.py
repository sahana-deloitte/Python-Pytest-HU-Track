class Admin:
    added_movies = []
    movie_timings = {}

    def adminscreen(self):
        username = "admin"
        password = "admin123"
        while True:

            Username = input("Enter Your Username:- ")
            Password = input("Enter Your Password:- ")
            if Username == username and Password == password:
                while True:
                    print("\t\t_________________________________________")
                    print("\t\t\t -------Admin Screen-------")
                    print("\t\t_________________________________________")
                    print("\t\t\t1-> Add Movie info")
                    print("\t\t\t2-> Edit movie info")
                    print("\t\t\t3-> Delete Movie")
                    print("\t\t\t4-> Logout")
                    choice2 = eval(input("\t\t\tEnter your choice(1/2/3/4):- "))
                    if choice2 == 1:
                        self.add_movies()
                    elif choice2 == 2:
                        self.edit_movies()
                    elif choice2 == 3:
                        self.delete_movies()
                    elif choice2 == 4:
                        break
                    else:
                         print("Invalid input ")
            else:
                print("Wrong Password.")
                print("1-> Try again")
                print("2-> Quit program")
                choice = eval(input("Enter your choice:- "))
                if choice == 2:
                    print("Quitting the program...")
                    break

            break

    def add_movies(self):

        Movies = {"title": " ", "genre": " ", "length": 0, "cast": " ", "director": " ", "rating": 0, "language": " ",
                  "shows": 0, "first_show": 0, "interval": 0, "gap": 0, "capacity": 0}
        timings = []

        mov_name = input("Enter the name of the movie to be added:- ")
        mov_name = mov_name.upper()
        Movies.update({"title": mov_name})

        mov_genre = input("Enter the genre of the movie:- ")
        Movies.update({"genre": mov_genre})

        mov_length = eval(input("Enter the length of the movie(in minutes):- "))
        Movies.update({"length": mov_length})

        mov_cast = input("Enter the cast of the movie:- ")
        Movies.update({"cast": mov_cast})

        mov_director = input("Enter the director of the movie:- ")
        Movies.update({"director": mov_director})

        mov_rating = eval(input("Enter the movie rating out of 10:- "))
        Movies.update({"rating": mov_rating})

        mov_lang = input("Enter the language of the movie:- ")
        Movies.update({"language": mov_lang})

        no_shows = eval(input("Enter number of shows:- "))
        Movies.update({"shows": no_shows})

        show_hr = int(input("Enter first show hour :- "))
        show_mn = int(input("Enter first show minutes:- "))
        first_show = "{}:{}".format(show_hr, show_mn)
        Movies.update({"first_show": first_show})

        interval = eval(input("Enter interval time:- "))
        Movies.update({"interval": interval})

        gap = eval(input("Enter gap between shows:- "))
        Movies.update({"gap": gap})

        capacity = eval(input("Enter seating capacity:- "))
        Movies.update({"capacity": capacity})

        print(Movies)
        self.added_movies.append(Movies)
        total_runtime = mov_length + interval + gap
        hours = total_runtime // 60
        minutes = total_runtime % 60
        time = "{}:{}".format(hours, minutes)
        show_hr_up = show_hr
        show_mn_up = show_mn
        start_time = first_show
        for initial in range(no_shows):
            show_hr_up = show_hr_up + hours
            show_mn_up = show_mn_up + minutes
            temp_dict = {}
            if show_mn_up >= 60:
                show_hr_up += 1
                show_mn_up = show_mn_up - 60
            end_time = "{}:{}".format(show_hr_up, show_mn_up)
            st = start_time + "-" + end_time

            temp_dict.update({st: capacity})
            timings.append(temp_dict)

            temp={mov_name:timings}
            self.movie_timings.update(temp)
            start_time = end_time

        print(self.movie_timings)

    def edit_movies(self):
        if len(self.added_movies) == 0:
            print("First add the movie!! ")
            self.add_movies()
            return
        for initial in range(len(self.added_movies)):
            print(self.added_movies[initial]["title"])

        toEditTitle = input("Enter the movie title which you want to be updated ")
        if self.added_movies[initial]["title"] == toEditTitle:
            cont="y"
        else:
            self.edit_movies()
            return

        print("Enter which data you want to edit ")
        print(
            "1.Genre\n2.Cast\n3.Director\n4.Admin Rating\n5.Language\n6.Length\tTimings\tNumber of Shows\t.First "
            "Show\tInterval\tTimeGap\tCapacity")
        while "y":
            value = int(input("Enter your choice which you want to edit or -1 to exit\n "))

            if value == -1:
                break
            elif value == 1:
                new_genre = input("Enter the new genre\n ")
                for initial in range(len(self.added_movies)):
                    if self.added_movies[initial]["title"] == toEditTitle:
                        data = self.added_movies[initial]
                        data.update({"genre": new_genre})
                        print("Updated")
                        break

            elif value == 2:
                new_cast = input("Enter the new cast\n ")
                for initial in range(len(self.added_movies)):
                    if self.added_movies[initial]["title"] == toEditTitle:
                        data = self.added_movies[initial]
                        data.update({"cast": new_cast})
                        print("Updated")
                        break
            elif value == 3:
                new_director = input("Enter the new director\n ")
                for initial in range(len(self.added_movies)):
                    if self.added_movies[initial]["title"] == toEditTitle:
                        data = self.added_movies[initial]
                        data.update({"director": new_director})
                        print("Updated")
                        break

            elif value == 4:
                new_rating = input("Enter the new rating\n ")
                for initial in range(len(self.added_movies)):
                    if self.added_movies[initial]["title"] == toEditTitle:
                        data = self.added_movies[initial]
                        data.update({"rating": new_rating})
                        print("Updated")
                        break
            elif value == 5:
                new_lang = input("Enter the new language\n ")
                for initial in range(len(self.added_movies)):
                    if self.added_movies[initial]["title"] == toEditTitle:
                        data = self.added_movies[initial]
                        data.update({"language": new_lang})
                        print("Updated")
                        break

            elif value == 6:
                new_length =int(input("Enter the new length\n "))
                new_no_shows = int(input("Enter the new no of shows\n "))
                show_hr = int(input("Enter first show hour :-\n "))
                show_mn = int(input("Enter first show minutes:-\n "))
                first_show = "{}:{}".format(show_hr, show_mn)
                new_interval = int(input("Enter the new interval\n "))
                new_gap = int(input("Enter the new gap\n "))
                new_capacity = int(input("Enter the new capacity\n "))
                timings=[]

                total_runtime = new_length + new_interval + new_gap
                hours = total_runtime // 60
                minutes = total_runtime % 60
                time = "{}:{}".format(hours, minutes)
                show_hr_up = show_hr
                show_mn_up = show_mn
                start_time = first_show
                for initial in range(new_no_shows):
                    show_hr_up = show_hr_up + hours
                    show_mn_up = show_mn_up + minutes
                    temp_dict={}
                    if (show_mn_up >= 60):
                        show_hr_up += 1
                        show_mn_up = show_mn_up - 60
                    end_time = "{}:{}".format(show_hr_up, show_mn_up)
                    st = start_time + "-" + end_time

                    temp_dict.update({st: new_capacity})
                    timings.append(temp_dict)

                    temp = {toEditTitle: timings}
                    del self.movie_timings[toEditTitle]
                    self.movie_timings.update(temp)
                    start_time = end_time

                for initial in range(len(self.added_movies)):
                    if self.added_movies[initial]["title"] == toEditTitle:
                        data = self.added_movies[initial]
                        data.update({"length": new_length})
                        data.update({"shows": new_no_shows})
                        data.update({"interval":new_interval})
                        data.update({"gap":new_gap})

                        print("Updated")
                        break

            print(self.added_movies)
            print(self.movie_timings)

    def delete_movies(self):
        if len(self.added_movies) == 0:
            print("First add the Movie details:- ")
            self.add_movies()
            return
        print("List of movies")
        for initial in range(len(self.added_movies)):
            print(self.added_movies[initial]["title"])
        toDeleteMovie = input("Enter the movie name to be deleted:- ")
        flag = 0
        flag1 = 0
        for initial in range(len(self.added_movies)):
            if self.added_movies[initial]["title"] == toDeleteMovie:
                del self.added_movies[initial]
                flag = 1
                flag1 = 1
                break
        if flag == 0:
            print("enter correct details")
            self.delete_movies()
        if flag1:
            print(self.added_movies)