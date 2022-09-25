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


def implementing_customers_days_and_food(file_lines):
    customers_dicts = get_restaurant_customers(file_lines)
    customers = list(customers_dicts.keys())

    for line in file_lines:
        for customer in customers:
            if customer in line:
                customers_dicts[customer]['days'].append(line[2])
                customers_dicts[customer]['foods'].append(line[1])

    return customers_dicts    


def maria_requested_food(file_lines):
    count_food = 0
    most_consumed_food = ''
    menu = get_restaurant_menu(file_lines)
    customers = implementing_customers_days_and_food(file_lines)

    for food in menu:
        final_count_food = customers['maria']['foods'].count(food)
        if final_count_food > count_food:
            count_food = final_count_food
            most_consumed_food = food

    return most_consumed_food


def times_arnaldo_ordered_hamburguers(file_lines):
    customers = implementing_customers_days_and_food(file_lines)

    return str(customers['arnaldo']['foods'].count('hamburguer'))


def foods_that_joao_never_asked(file_lines):
    foods_never_asked = set()
    menu = get_restaurant_menu(file_lines)
    customers = implementing_customers_days_and_food(file_lines)

    for food in menu:
        if food not in customers['joao']['foods']:
            foods_never_asked.add(food)

    return str(foods_never_asked)

    
def analyze_log(path_to_file):
    raise NotImplementedError
