from datetime import date
from application.db.people import get_employees
from application.salary import calculate_salary


class AccountManager:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def print_hi(self):
        name = self.name
        print(f'Hi, {name}')

def main():
    accountmeneger = AccountManager('Jhon', '12345')
    accountmeneger.print_hi()
    calculate_salary(accountmeneger.name)
    get_employees(accountmeneger.name)
    print(date.today().strftime("%d.%m.%Y"))


if __name__ == '__main__':

    main()





