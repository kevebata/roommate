class Roommate:
    # class variable
    univ_name = "University of California, Santa Cruz"
    # __init__ function stores data variables, self.__name and self.__collegename
    def __init__(self, name, collegename):
        self.__name = name
        self.__collegename = collegename
    # get_name function returns roommate's name
    def get_name (self):
        return f"Your roommate's name is {self.__name}."
    # get_collegename function returns the name of the college the roommate is affiliated with at UCSC
    def get_collegename (self):
        return f"Your roommate is affiliated with {self.__collegename} at {Roommate.univ_name}."
    # rating function returns the number of times the roommate has disturbed the user and list any repeated 
    # activities the roommate has done that annoyed the user
    def rating(self, behaviorrecord):
        self.__behaviorrecord = behaviorrecord
        # this for loop is basically a counter
        counter = 0
        emptylist = []
        repeat = []
        # goes every "complain" in the list
        for every_complain in self.__behaviorrecord:
            # adds one to the counter
            counter += 1
            every_complain = every_complain.strip()
            every_complain = every_complain.upper()
            # basically this adds every complain into an empty list and see if there are any repeats and puts all
            # the repeats into one list
            if every_complain not in emptylist:
                emptylist.append(every_complain)
            else:
                if every_complain not in repeat:
                    repeat.append(every_complain)
                else:
                    pass
        # statement that has counter
        annoying_counter = f"This is the number of times your roommate has disturbed you: {counter}"
        # this for loop puts the repeat list into a string
        repeats = ""
        rcounter = 0
        for i in repeat:
            rcounter += 1
            i = i.title()
            repeats += f"{i}, "
        repeats = repeats[:-2]
        # if there are no repeats, return just the counter message
        if rcounter == 0:
            return annoying_counter
        # else, return counter message and also repeat message stating what activities
        # the roommate has repeated that annoyed the user
        else:
            repeat_statement = f"These are some activities your roommate repeated that annoyed you: {repeats}"
            return f"{annoying_counter}\n{repeat_statement}"
    # function that tells the amount of freetime the roommate has
    def freetime(self, occupied_time):
        self.__occupied_time = occupied_time
        # checks if user input is valid since you can't go over 24 hours (returns error message and None)
        if occupied_time > 24:
            print("Impossible! Only 24 hours in day! Try again")
            return None
        # calculates the freetime of the roommate
        freetime = 24 - self.__occupied_time
        # returns message with amount of freetime
        if freetime > 0:
            return f"This is the amount of free time your roommate has: {freetime} hours"
        # if freetime is 0, then return this message
        else:
            return f"Your roommate has no freetime :( <-- sad emoji!"
# the main function
def main():
    # input for roommate's name
    name = input("Enter your roommate's name here: ")
    # input for roommate's college
    college = input("Enter the college your roommate is affiliated with: ")
    roomie = Roommate(name, college)
    nroomie = roomie.get_name()
    croomie = roomie.get_collegename()
    # input for list consisting disturbing activities
    list_input = input("List activities your roommate has done that has annoyed you\n(ex: cussing, snoring, and etc) [format like: snoring, cussing, cussing, eating loud]: ")
    list_input = list(list_input.split(", "))
    myrating = roomie.rating(list_input)
    # input for roommate's amount of occupied hours
    occupied_time = int(input("Enter the amount of time (in hours but input just number) your roommate is occupied for in a day: "))
    rfreetime = roomie.freetime(occupied_time)
    # print results
    print(nroomie)
    print(croomie)
    print(myrating)
    print(rfreetime)

# to run main function
if __name__ == "__main__":
    main()
