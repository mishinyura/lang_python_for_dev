class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self._stock = stock

    def __repr__(self) -> str:
        return self.name

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, count: int) -> None:
        self._stock = count

    def update_stock(self, quantity: int) -> None:
        if self.stock + quantity < 0:
            raise Exception('Недостаточно товара на складе')
        self.stock += quantity

class Order:
    def __init__(self) -> None:
        self.order = {}

    def add_product(self, product: Product, quantity: int) -> None:
        try:
            product.update_stock(-quantity)
        except Exception as ex:
            print(ex)
        else:
            self.order[product] = quantity

    def remove_product(self, product: Product, quantity: int) -> None:
        if self.order[product] - quantity <= 0:
            self.order.pop(product)
        else:
            self.order[product] -= quantity
        product.update_stock(quantity)

    def calculate_total(self) -> float:
        total_lst = [product.price * amount for product, amount in self.order.items()]
        return round(float(sum(total_lst)), 2)



class Store:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def list_products(self) -> None:
        print(self.products)

    def create_order(self) -> Order:
        order = Order()
        return order

def info(product: Product, order: Order, action: str) -> None:
    """Вывод данные о состоянии продукта и показателях заказа."""
    print("Товар '{0}' - {1}:"
          "\n-\tОстаток на складе: {2}"
          "\n-\tОстаток в магазине: {3}"
          "\n-\tОбщая стоимость заказа: {4}".format(
        product,
        action,
        product.stock,
        order.order.get(product, 0),
        order.calculate_total()
    ))

def main() -> None:
    # Создаем магазин
    store = Store()

    # Создаем товары
    prod_laptop = Product("Ноутбук", 1000, 5)
    prod_smartphone = Product("Смартфон", 500, 10)
    prod_tablet = Product("Планшет", 650, 8)
    prod_headphones = Product("Наушники", 200, 15)

    # Добавляем товары в магазин
    products = [prod_laptop, prod_smartphone, prod_tablet, prod_headphones]
    for prod in products:
        store.add_product(prod)

    # Список всех товаров магазине
    store.list_products()

    # Создаем заказ
    order = store.create_order()
    info(prod_headphones, order, 'Создаем заказ')

    # Добавляем товары в заказ
    for prod in products:
        order.add_product(prod, prod.stock)
    info(prod_headphones, order, 'Добавляем товары в заказ')

    # Удаляем из заказа товар
    order.remove_product(prod_headphones, 15)
    info(prod_headphones, order, 'Удаляем из заказа товар')

    order.remove_product(prod_laptop, 3)
    info(prod_laptop, order, 'Удаляем из заказа товар')

    # Проверяем остатки на складе после заказа
    store.list_products()

if __name__ == '__main__':
    main()