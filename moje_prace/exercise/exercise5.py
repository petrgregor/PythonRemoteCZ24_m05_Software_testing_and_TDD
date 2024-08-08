class Product:
    def __init__(self, name: str, volume: float):
        self.name = name
        self.volume = volume


class Warehouse:
    def __init__(self, capacity: float):
        self.capacity = capacity
        self.products = []

    def __calculate_free_space(self):
        sum_od_products = sum([x.volume for x in self.products])
        return self.capacity - sum_od_products

    def add(self, product: Product):
        rest_space = self.__calculate_free_space()
        if rest_space >= product.volume:
            self.products.append(product)
            return rest_space - product.volume
        else:
            return -1