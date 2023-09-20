"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev department", "name": "sales", "value_percents": 20},
]

def show_all_departments():
    """1. Вывести названия всех отделов"""
    department_list = [department["title"] for department in departments]
    print(f"Названия всех отделов: {', '.join(department_list)}")


def show_all_employees():
    """2. Вывести имена всех сотрудников компании."""
    names_list = []
    for department in departments:
        for employee in department["employers"]:
            names_list.append(f"{employee['first_name']} {employee['last_name']}")
    print(f"Имена всех сотрудников компании: {', '.join(names_list)}")


def show_all_employees_and_departments():
    """3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают."""
    names_list = []
    for department in departments:
        for employee in department["employers"]:
            names_list.append(f"{employee['first_name']} {employee['last_name']} ({department['title']})")
    print(f"Имена всех сотрудников компании c указанием отдела: {', '.join(names_list)}")


def show_names_above_100k():
    """4. Вывести имена всех сотрудников компании, которые получают больше 100к."""
    names_list = []
    for department in departments:
        for employee in department["employers"]:
            if employee['salary_rub'] > 100_000:
                names_list.append(f"{employee['first_name']} {employee['last_name']}")
    print(f"Имена всех сотрудников компании, которые получают больше 100к.: {', '.join(names_list)}")


def show_positions_below_80k():
    """5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями)."""
    position_list = []
    for department in departments:
        for employee in department["employers"]:
            if employee['salary_rub'] < 80_000 and employee['position'] not in position_list:
                position_list.append(f"{employee['position']}")
    print(f"Позиции, на которых люди получают меньше 80к: {', '.join(position_list)}")


def show_departments_costs():
    """6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела."""
    salary_list = []
    for department in departments:
        month_costs = 0
        for employee in department["employers"]:
            month_costs += employee['salary_rub']
        salary_list.append(f"{department['title']} -- {str(month_costs)}")
    print(f"Сколько денег в месяц уходит на каждый отдел: {', '.join(salary_list)}")


def show_department_min_salary():
    """7. Вывести названия отделов с указанием минимальной зарплаты в нём."""
    salary_list = []
    for department in departments:
        month_costs = []
        for employee in department["employers"]:
            month_costs.append(employee['salary_rub'])
        salary_list.append(f"{department['title']} -- {min(month_costs)}")
    print(f"Названия отделов с указанием минимальной зарплаты в нём: {', '.join(salary_list)}")


def show_department_min_average_max_salary():
    """8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём."""
    salary_list = []
    for department in departments:
        month_costs = []
        for employee in department["employers"]:
            month_costs.append(employee['salary_rub'])
        salary_list.append(f"{department['title']}: min - {min(month_costs)}, average - {sum(month_costs) // len(month_costs)}, max - {max(month_costs)}")
    print(f"Названия отделов с указанием минимальной, средней и максимальной зарплаты в нём: {'; '.join(salary_list)}")


def show_company_average_salary():
    """9. Вывести среднюю зарплату по всей компании."""
    salary_list = []
    for department in departments:
        for employee in department["employers"]:
            salary_list.append(employee['salary_rub'])
    print(f"Cредняя зарплата по всей компании: {sum(salary_list) // len(salary_list)}")


def show_positions_above_90k():
    """10. Вывести названия должностей, которые получают больше 90к без повторений."""
    position_list = []
    for department in departments:
        for employee in department["employers"]:
            if employee['salary_rub'] > 90_000 and employee['position'] not in position_list:
                position_list.append(f"{employee['position']}")
    print(f"Названия должностей, которые получают больше 90к: {', '.join(position_list)}")


def show_average_women_salary_by_department():
    """11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин)."""
    women = ("Michelle", "Nicole", "Christina", "Caitlin")
    salary_list = []
    for department in departments:
        month_costs = []
        for employee in department["employers"]:
            if employee['first_name'] in women:
                month_costs.append(employee['salary_rub'])
        salary_list.append(f"{department['title']} -- {sum(month_costs) // len(month_costs)}")
    print(f"Cредняя зарплата по каждому отделу среди девушек: {', '.join(salary_list)}")


def show_names_ending_with_vowel():
    """12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву."""
    vowels = 'aeiouy'
    name_list = []
    for department in departments:
        for employee in department["employers"]:
            if employee['last_name'][-1] in vowels and employee['position'] not in name_list:
                name_list.append(f"{employee['first_name']} {employee['last_name']}")
    print(f"Имена людей, чьи фамилии заканчиваются на гласную букву: {', '.join(name_list)}")


def show_average_tax():
    """13. Вывести список отделов со средним налогом на сотрудников этого отдела."""
    tax_list = []
    for department in departments:
        month_tax = []
        for employee in department["employers"]:
            tax_per_employee = 0
            for tax in taxes:
                if tax['department'] == None:
                    tax_per_employee += tax['value_percents']
                elif tax['department'] == department['title']:
                    tax_per_employee += tax['value_percents']
            month_tax.append(tax_per_employee)
        tax_list.append(f"{department['title']}  - {sum(month_tax) // len(month_tax)}%")
    print(f"Список отделов со средним налогом на сотрудников этого отдела: {'; '.join(tax_list)}")


def show_employees_salary():
    """14. Вывести список всех сотрудников с указанием зарплаты "на руки" и зарплаты с учётом налогов."""
    names_list = []
    for department in departments:
        for employee in department["employers"]:
            tax_per_employee = 0
            for tax in taxes:
                if tax['department'] == None:
                    tax_per_employee += tax['value_percents']
                elif tax['department'] == department['title']:
                    tax_per_employee += tax['value_percents']
            salary_with_tax = employee['salary_rub']
            salary_on_hands = salary_with_tax - (salary_with_tax * tax_per_employee // 100)
            names_list.append(f"{employee['first_name']} {employee['last_name']} {salary_on_hands}/{salary_with_tax}")
    print(f"Cписок всех сотрудников с указанием зарплаты 'на руки' и зарплаты с учётом налогов: {', '.join(names_list)}")


def show_department_taxes():
    """15. Вывести список отделов, отсортированный по месячной налоговой нагрузке."""
    department_list = []
    for department in departments:
        tax_per_department = []
        for employee in department["employers"]:
            percent_of_tax_per_employee = 0
            for tax in taxes:
                if tax['department'] == None:
                    percent_of_tax_per_employee += tax['value_percents']
                elif tax['department'] == department['title']:
                    percent_of_tax_per_employee += tax['value_percents']
            tax_per_employee = employee['salary_rub'] * percent_of_tax_per_employee // 100
            tax_per_department.append(tax_per_employee)
        department_list.append(f"{sum(tax_per_department)} -- {department['title']}")
    print(f"Cписок отделов, отсортированный по месячной налоговой нагрузке: {', '.join(sorted(department_list))}")


def show_taxes_above_100k_names():
    """16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год."""
    names_list = []
    for department in departments:
        for employee in department["employers"]:
            tax_per_employee_per_month = 0
            for tax in taxes:
                if tax['department'] == None:
                    tax_per_employee_per_month += tax['value_percents']
                elif tax['department'] == department['title']:
                    tax_per_employee_per_month += tax['value_percents']
            tax_per_employee_per_year = employee['salary_rub'] * tax_per_employee_per_month // 100 * 12
            if tax_per_employee_per_year > 100_000:
                names_list.append(f"{employee['first_name']} {employee['last_name']}")
    print(f"Список всех сотрудников, за которых компания платит больше 100к налогов в год: {', '.join(names_list)}")


def show_least_tax_name():
    """17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов."""
    name = ''
    minimal_tax = []
    for department in departments:
        for employee in department["employers"]:
            tax_perscent_per_month = 0
            for tax in taxes:
                if tax['department'] == None:
                    tax_perscent_per_month += tax['value_percents']
                elif tax['department'] == department['title']:
                    tax_perscent_per_month += tax['value_percents']
            tax_per_month = employee['salary_rub'] * tax_perscent_per_month // 100
            minimal_tax.append(tax_per_month)
            if tax_per_month == min(minimal_tax):
                name = f"{employee['first_name']} {employee['last_name']}"
    print(f"Имя и фамилия сотрудника, за которого компания платит меньше всего налогов: {name}")


def main():
    # 1. Вывести названия всех отделов.
    show_all_departments()
    # 2. Вывести имена всех сотрудников компании.
    show_all_employees()
    # 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
    show_all_employees_and_departments()
    # 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
    show_names_above_100k()
    # 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
    show_positions_below_80k()
    # 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
    show_departments_costs()
    # 7. Вывести названия отделов с указанием минимальной зарплаты в нём.
    show_department_min_salary()
    # 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
    show_department_min_average_max_salary()
    # 9. Вывести среднюю зарплату по всей компании.
    show_company_average_salary()
    # 10. Вывести названия должностей, которые получают больше 90к без повторений.
    show_positions_above_90k()
    # 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
    show_average_women_salary_by_department()
    # 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
    show_names_ending_with_vowel()
    # 13. Вывести список отделов со средним налогом на сотрудников этого отдела.
    show_average_tax()
    # 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
    show_employees_salary()
    # 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
    show_department_taxes()
    # 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
    show_taxes_above_100k_names()
    # 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
    show_least_tax_name()


if __name__ == '__main__':
    main()
