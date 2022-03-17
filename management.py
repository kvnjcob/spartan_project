from spartan import Spartan

spartan_dict = {}


def read_option():
    while True:
        print("============================================================")
        print("1. Add an spartan\n2. Remove an spartan\n3. List the spartans\n"
              "4. Retrieve spartan information by Id\n5. Exit")
        print("============================================================")
        user_input_str = input("Please enter your input : ")
        user_input_str.strip()

        if user_input_str in ["1", "2", "3", "4", "5"]:
            user_input_str.strip()
            return user_input_str
        else:
            print("Please enter a valid option from 1 to 5")


def read_first_name():
    while True:
        emp_first_name = input("Please enter the employee first name : ")
        emp_first_name.strip()

        if len(emp_first_name) >= 2:
            return emp_first_name
        elif emp_first_name.isdigit():
            print("Name must have at least two alphabets")
        else:
            print("Please enter a valid first name with at least 2 characters")


def read_last_name():
    while True:
        emp_second_name = input("Please enter the employee second name : ")
        emp_second_name.strip()

        if len(emp_second_name) >= 2:
            return emp_second_name
        elif emp_second_name.isdigit():
            print("Name must have at least two alphabet")
        else:
            print("Please enter a valid second name with at least 2 characters")


def read_birth_year():
    while True:
        birth_year = input("Please enter the year of birth : ")
        birth_year.strip()

        if birth_year.isdigit():
            year = int(birth_year)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Enter a year of birth between 1900 and 2004")
        else:
            print("Please enter a valid year")


def read_birth_month():
    while True:
        birth_month = input("Please enter the month you were born : ")
        birth_month.strip()

        if birth_month.isdigit():
            month = int(birth_month)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Please enter a month from 1 to 12")
        else:
            print("Please enter a valid month")


def read_birth_day():
    while True:
        day_str = input("Please Enter the day you were born :")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The Birth Day should be between 1 and 31")
        else:
            print("Please enter a valid day")


def read_course():
    while True:
        course = input("Please Enter The opted course : ")
        course.strip()

        if len(course) >= 1:
            return course
        else:
            print("Please enter a valid course")


def read_stream():
    while True:
        stream = input("Please Enter The oped stream :")
        stream.strip()

        if len(stream) >= 1:
            return stream
        else:
            print("Please enter a valid stream")


def read_id():
    id_str = input("Please enter an id : ")
    id_str.strip()

    if id_str.isdigit():
        id1 = int(id_str)
        if id1 > 0:
            return id1
        else:
            print("You have entered a negative digit for id")
    else:
        print("Please enter a numeric id, no alphabets allowed")


def add_spartan():
    global spartan_dict

    first_name = read_first_name()
    last_name = read_last_name()
    birth_year = read_birth_year()
    birth_month = read_birth_month()
    birth_day = read_birth_day()
    course = read_course()
    stream = read_stream()
    spartan_id = read_id()

    spartan = Spartan(spartan_id, first_name, last_name, birth_year, birth_month, birth_day, course,
                      stream)

    emp_id_key = spartan.get_spartan_id()
    spartan_dict[emp_id_key] = spartan

    print(spartan)


def remove_spartan():
    user_id = read_id()

    if user_id in spartan_dict:
        del spartan_dict[user_id]
        print("The employee is removed")
    else:
        print("Could not find the Id")


def retrieve_spartan():
    retrieve_id = read_id()
    if retrieve_id in spartan_dict:
        print(spartan_dict[retrieve_id])
    else:
        print("The id you entered does not exist")


def list_spartans():
    for spartan_id in spartan_dict:
        print(spartan_dict[spartan_id])




