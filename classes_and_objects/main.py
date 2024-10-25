class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self._stock = stock

    def __repr__(self):
        return self.name

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, count):
        self._stock = count

    def update_stock(self, quantity: int):
        if self.stock - quantity < 0:
            raise Exception('Недостаточно товара на складе')
        self.stock -= quantity

class Order:
    def __init__(self):
        self.order = {}

    def add_product(self, product: Product, quantity: int):
        try:
            product.update_stock(quantity)
        except Exception as ex:
            print(ex)
        else:
            self.order[product] = quantity

    def calculate_total(self):
        return sum(product.price * amount for product, amount in self.order.items())



class Store:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def list_products(self) -> None:
        print(self.products)

    def create_order(self):
        order = Order()
        return order

def main():
    # Создаем магазин
    store = Store()

    # Создаем товары
    product1 = Product("Ноутбук", 1000, 5)
    product2 = Product("Смартфон", 500, 10)

    # Добавляем товары в магазин
    store.add_product(product1)
    store.add_product(product2)

    # Список всех товаров
    store.list_products()

    # Создаем заказ
    order = store.create_order()

    # Добавляем товары в заказ
    order.add_product(product1, 2)
    order.add_product(product2, 3)

    # Выводим общую стоимость заказа
    total = order.calculate_total()
    print(f"Общая стоимость заказа: {total}")

    # Проверяем остатки на складе после заказа
    store.list_products()

if __name__ == '__main__':
    main()