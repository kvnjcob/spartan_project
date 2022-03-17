class Spartan:
    def __init__(self, spartan_id, spartan_first_name, spartan_last_name, birth_year, birth_month, birth_day, course,
                 stream):
        self.spartan_id = spartan_id
        self.first_name = spartan_first_name
        self.last_name = spartan_last_name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.course = course
        self.stream = stream

    def get_spartan_id(self):
        return self.spartan_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_year(self):
        return self.birth_year

    def get_birth_month(self):
        return self.birth_month

    def get_birth_day(self):
        return self.birth_day

    def get_course(self):
        return self.course

    def get_stream(self):
        return self.stream

    def set_spartan_id(self, new_id):
        self.spartan_id = new_id

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_birth_year(self, new_birth_year):
        self.birth_year = new_birth_year

    def set_birth_month(self, new_birth_month):
        self.birth_month = new_birth_month

    def set_birth_day(self, new_birth_day):
        self.birth_day = new_birth_day

    def set_course(self, new_course):
        self.course = new_course

    def set_stream(self, new_stream):
        self.stream = new_stream

    def __str__(self):
        return f"Spartan ID: {self.spartan_id} - First Name: {self.first_name} - Last Name: {self.last_name} - " \
               f"Birth year: {self.birth_year} - Birth month: {self.birth_month} - Birth day: {self.birth_day} -" \
               f"Course: {self.course} - Stream: {self.stream}"

