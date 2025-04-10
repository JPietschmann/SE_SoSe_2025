class Person ():
 def __init__(self, first_name: str, last_name: str):
    self.first_name= first_name
    self.last_name=  last_name
    pass

class Subject (Person):
    def __init__ (self, first_name: str, last_name: str, date_of_birth: str, age: int, sex: str):
        super.__init__ (first_name, last_name)
        self.__date_of_birth= date_of_birth
        self.age= age
        self.sex= sex
        pass

    def estimate_max_hr(self): 
        if self.sex == "male":
            max_hr_bpm = 223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * self.age
        else:
            max_hr_bpm = input("Enter maximum heart rate:")
        return max_hr_bpm

class Supervisor (Person):
        pass

class Experiment ():
    def __init__(self, test_id: str, date: str):
        self.test_id= test_id
        self.date= date

    def add_subject(self, subject):
        self.subject = subject
        return 

    def add_supervisor(self, supervisor):
        self.supervisor= supervisor
        return