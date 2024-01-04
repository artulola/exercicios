class Product:
    def __init__(self, code, value, description):
        self.__code = code
        self.__value = value
        self.__description = description

    def get_value(self):
        return self.__value

class ProductItem:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def get_product(self):
        return self.__product

class Order:
    def __init__(self):
        self.__total_value = 0.0
        self.__order_items = []

    def add_item(self, item):
        self.__order_items.append(item)

    def get_total(self):
        for item in self.__order_items:
            self.__total_value += float(item.get_quantity()) * float(item.get_product().get_value())
        return self.__total_value

if __name__ == '__main__':
    prod1 = Product(1, 3.00, "Chilito")
    prod2 = Product(2, 3.00, "Coxinha")
    prod3 = Product(3, 5.00, "Coca-cola")
    item_prod = ProductItem(prod1, 3)
    item_prod1 = ProductItem(prod2, 2)
    item_prod2 = ProductItem(prod3, 2)
    order = Order()
    order.add_item(item_prod)
    order.add_item(item_prod1)
    order.add_item(item_prod2)
    print("Total:", order.get_total())
