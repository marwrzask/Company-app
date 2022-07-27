
class Employer:
    #conctructor
    def __init__(self, first_name, last_name, age, job, salary, employer_id, bonus=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus
        self.total_salary = salary + bonus
        self.employer_id = employer_id

    #method -- add bonus
    def apply_bonus(self, bonus_value):
        self.bonus += bonus_value
        self.total_salary = self.salary + self.bonus

class Department:

    def __init__(self, name):
        self.name = name #department name
        self.employers = [] #list of users in current department

    def add_employer(self, new_employer): #add employer to current department
        self.employers.append(new_employer)

    def display_employers(self):
        for i in self.employers:
            print(i.first_name, i.last_name)


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employers = []
        self.departments = {}

    def create_department(self, name):
        self.departments[name] = Department(name)

    def create_employers(self, first_name, last_name, age, job, salary, bonus):
        self.employers.append(Employer(first_name, last_name, age, job, salary, len(self.employers), bonus))

    def add_bonus(self, employer_id, bonus_value):
        self.employers[employer_id].apply_bonus(bonus_value)

    def delete_employers(self, employer_id):
        self.employers.remove(self.employers[employer_id])

    def display_department(self):
        print(list(company.departments.keys()))


if __name__ == '__main__':

    company = Company('Capgemini')
    company.create_department('IT')
    company.create_department('WG')
    company.create_department('EARTH')

    company.create_employers('Basia', 'Stanko', 28, 'Developer', 1500, bonus=500)
    company.create_employers('Jan', 'Kowalski', 25, 'Developer', 500, bonus=100)
    company.create_employers('Bartek', 'Jasina', 25, 'Developer', 500, bonus=100)
    company.add_bonus(0,2000)

    company.departments['IT'].add_employer(company.employers[0])
    company.departments['IT'].add_employer(company.employers[1])
    company.departments['IT'].add_employer(company.employers[2])

    print(company.employers[0].total_salary)
    print(company.employers[0].first_name)
    #company.delete_employers(0)

    company.departments['IT'].display_employers()
    company.display_department()

