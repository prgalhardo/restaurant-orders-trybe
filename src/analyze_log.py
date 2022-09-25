import csv


# Requisito 1 realizado com a ajuda do aluno João Lenny, Turma 16 Tribo A.
def get_days_that_the_restaurant_opens(file_lines):
    days = set()

    for line in file_lines:
        days.add(line[2])
    
    return days


def get_restaurant_menu(file_lines):
    menu = set()

    for line in file_lines:
        menu.add(line[1])

    return menu


def get_restaurant_customers(file_lines):
    customers = set()
    customers_dicts = dict()

    for line in file_lines:
        customers.add(line[0])
    
    for customer in customers:
        customers_dicts[customer] = {'days': [], 'foods': []}

    return customers_dicts


def implementing_days_and_food(file_lines):
    customers_dicts = get_restaurant_customers(file_lines)
    customers = list(customers_dicts.keys())

    for line in file_lines:
        for customer in customers:
            if customer in line:
                customers_dicts[customer]['days'].append(line[2])
                customers_dicts[customer]['foods'].append(line[1])

    return customers_dicts    


def analyze_log(path_to_file):
    raise NotImplementedError
