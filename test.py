class Company:
    def __init__(self):
        self.work = True
        self.name = 'Jane'
        self.gender = 'woman'
    def retire(self):
        self.work = False
class Employee(Company):
    def __init__(self, name, gender):
        super().__init__()
        self.name = name
        self.gender = gender
    def introduce(self):
        if self.work == True:
            print('I got a job at a company')
            print('My name is', self.name)
            print('I am a', self.gender)
        if self.work == False:
            print('I left the company')
