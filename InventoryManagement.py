warehouses = {
    "Warehouse A": {"Laptop": 10, "Mouse": 25, "Keyboard": 5},
    "Warehouse B": {"Laptop": 5, "Mouse": 10, "Keyboard": 20},
    "Warehouse C": {"Laptop": 15, "Mouse": 5, "Keyboard": 10}
}

reorder_level = 5


def add_product(warehouse, product, quantity):
    if quantity <= 0:
        print("Invalid quantity")
        return

    warehouses[warehouse][product] = warehouses[warehouse].get(product, 0) + quantity
    print(quantity, product, "added to", warehouse)


def remove_product(warehouse, product, quantity):
    if quantity <= 0:
        print("Invalid quantity")
        return

    if product not in warehouses[warehouse]:
        print("Product not found")
        return

    if warehouses[warehouse][product] < quantity:
        print("Insufficient inventory")
        return

    warehouses[warehouse][product] -= quantity
    print(quantity, product, "removed from", warehouse)


def transfer_stock(product, quantity, source, destination):
    if warehouses[source].get(product, 0) < quantity:
        print("Insufficient stock for transfer")
        return

    warehouses[source][product] -= quantity
    warehouses[destination][product] = warehouses[destination].get(product, 0) + quantity
    print("Stock transferred successfully")


def low_stock():
    print("\nLow Stock Products:")
    for warehouse, products in warehouses.items():
        for product, quantity in products.items():
            if quantity <= reorder_level:
                print(warehouse, "-", product, ":", quantity)


def find_warehouse(product, quantity):
    for warehouse, products in warehouses.items():
        if products.get(product, 0) >= quantity:
            print("Order should be fulfilled from:", warehouse)
            return warehouse

    print("No warehouse has sufficient stock")
    return None


print("Initial Inventory:")

for warehouse, products in warehouses.items():
    print(warehouse, products)

add_product("Warehouse A", "Mouse", 10)
remove_product("Warehouse B", "Laptop", 2)
transfer_stock("Keyboard", 5, "Warehouse C", "Warehouse A")
find_warehouse("Laptop", 8)
low_stock()

print("\nFinal Inventory:")

for warehouse, products in warehouses.items():
    print(warehouse, products)
