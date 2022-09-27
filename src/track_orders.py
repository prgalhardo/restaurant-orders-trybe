class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        dish = list()

        for line in self.orders:
            if line[0] == customer:
                dish.append(line[1])

        most_ordered_dish = max(dish, key=dish.count)

        return most_ordered_dish

    def get_never_ordered_per_customer(self, customer):
        all_dishes = set()
        customer_dishes = set()

        for line in self.orders:
            all_dishes.add(line[1])
            if line[0] == customer:
                customer_dishes.add(line[1])

        never_ordered = all_dishes.difference(customer_dishes)

        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
