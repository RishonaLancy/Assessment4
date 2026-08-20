#1st
class DigitalWallet:
    def __init__(self, name, balance, daily_limit):
        self.name = name
        self.balance = balance
        self.daily_limit = daily_limit
        self.daily_total = 0
        self.transactions = []
        self.failed_pins = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return
        self.balance += amount
        self.transactions.append(("Deposit", amount))
        print("Deposit successful:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        if self.daily_total + amount > self.daily_limit:
            print("Daily transaction limit exceeded")
            return

        self.balance -= amount
        self.daily_total += amount
        self.transactions.append(("Withdrawal", amount))

        if amount > 50000:
            print("Suspicious transaction: Large amount")

        print("Withdrawal successful:", amount)

    def transfer(self, amount):
        if amount <= 0:
            print("Invalid transfer amount")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        if self.daily_total + amount > self.daily_limit:
            print("Daily transaction limit exceeded")
            return

        self.balance -= amount
        self.daily_total += amount
        self.transactions.append(("Transfer", amount))

        if amount > 50000:
            print("Suspicious transaction: Large transfer")

        print("Transfer successful:", amount)

    def verify_balance(self):
        print("Current Balance:", self.balance)

    def history(self):
        print("\nTransaction History:")
        for t in self.transactions:
            print(t[0], ":", t[1])

    def failed_pin(self):
        self.failed_pins += 1
        if self.failed_pins >= 3:
            print("Suspicious transaction: Multiple failed PIN attempts")


wallet = DigitalWallet("Rishikaa", 100000, 100000)

print("Account created for:", wallet.name)

wallet.deposit(10000)
wallet.withdraw(15000)
wallet.transfer(20000)

wallet.failed_pin()
wallet.failed_pin()
wallet.failed_pin()

wallet.withdraw(60000)

wallet.verify_balance()
wallet.history()



#2nd
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


#3rd
def calculate_fare(customer_id, distance, passengers, vehicle,
                   booking_time, driver_available, discount):

    print("Customer ID:", customer_id)

    if distance <= 0:
        print("Invalid distance")
        return

    if passengers <= 0 or passengers > 6:
        print("Invalid passenger count")
        return

    if not driver_available:
        print("No driver available")
        return

    if vehicle == "Bike":
        base_fare = 30
        rate = 8
    elif vehicle == "Sedan":
        base_fare = 50
        rate = 12
    elif vehicle == "SUV":
        base_fare = 70
        rate = 15
    elif vehicle == "Premium":
        base_fare = 100
        rate = 20
    else:
        print("Invalid vehicle type")
        return

    distance_fare = distance * rate

    peak_surcharge = 0
    if 8 <= booking_time <= 10 or 17 <= booking_time <= 20:
        peak_surcharge = 50

    night_surcharge = 0
    if booking_time >= 22 or booking_time < 6:
        night_surcharge = 40

    passenger_surcharge = 0
    if passengers > 4:
        passenger_surcharge = 30

    total = base_fare + distance_fare
    total += peak_surcharge + night_surcharge
    total += passenger_surcharge

    discount_amount = total * discount / 100
    final_fare = total - discount_amount

    print("Vehicle:", vehicle)
    print("Base Fare:", base_fare)
    print("Distance Fare:", distance_fare)
    print("Peak Surcharge:", peak_surcharge)
    print("Night Surcharge:", night_surcharge)
    print("Passenger Surcharge:", passenger_surcharge)
    print("Discount:", discount_amount)
    print("Final Fare:", final_fare)
    print("Driver assigned successfully")


calculate_fare(
    "C101",
    10,
    2,
    "Sedan",
    18,
    True,
    10
)


#4th
patients = [
    {
        "id": "P101",
        "age": 65,
        "oxygen": 85,
        "heart_rate": 120,
        "blood_pressure": 90,
        "temperature": 39,
        "condition": "Critical",
        "emergency": True
    },
    {
        "id": "P102",
        "age": 40,
        "oxygen": 96,
        "heart_rate": 80,
        "blood_pressure": 120,
        "temperature": 37,
        "condition": "Normal",
        "emergency": False
    },
    {
        "id": "P103",
        "age": 55,
        "oxygen": 90,
        "heart_rate": 105,
        "blood_pressure": 100,
        "temperature": 38,
        "condition": "High",
        "emergency": False
    }
]

icu_beds = 2


def calculate_priority(patient):
    score = 0

    if patient["oxygen"] < 90:
        score += 40
    elif patient["oxygen"] < 94:
        score += 20

    if patient["heart_rate"] > 120:
        score += 30
    elif patient["heart_rate"] > 100:
        score += 15

    if patient["blood_pressure"] < 90:
        score += 30
    elif patient["blood_pressure"] < 100:
        score += 15

    if patient["temperature"] > 39:
        score += 20
    elif patient["temperature"] > 38:
        score += 10

    if patient["condition"] == "Critical":
        score += 30
    elif patient["condition"] == "High":
        score += 20
    elif patient["condition"] == "Medium":
        score += 10

    if patient["emergency"]:
        score += 50

    return score


def classify(score):
    if score >= 80:
        return "CRITICAL"
    elif score >= 50:
        return "HIGH"
    elif score >= 25:
        return "MEDIUM"
    else:
        return "LOW"


for patient in patients:
    patient["score"] = calculate_priority(patient)
    patient["priority"] = classify(patient["score"])

patients.sort(key=lambda x: x["score"], reverse=True)

print("ICU Allocation\n")

for patient in patients:
    print("Patient ID:", patient["id"])
    print("Priority Score:", patient["score"])
    print("Classification:", patient["priority"])

    if icu_beds > 0:
        print("ICU Bed Allocated")
        icu_beds -= 1
    else:
        print("No ICU bed - Waiting List")

    print()


#5th
courses = {
    "DBMS": {
        "credits": 4,
        "prerequisite": "Programming",
        "time": "10:00"
    },
    "AI": {
        "credits": 4,
        "prerequisite": "Data Structures",
        "time": "11:00"
    },
    "ML": {
        "credits": 3,
        "prerequisite": "Statistics",
        "time": "10:00"
    },
    "Cloud": {
        "credits": 3,
        "prerequisite": "Networking",
        "time": "12:00"
    }
}

student_id = "S101"
semester = 5
credit_limit = 12

completed_courses = [
    "Programming",
    "Data Structures",
    "Statistics",
    "Networking"
]

selected_courses = ["DBMS", "AI", "ML"]

registered_courses = []


def register_course(course):

    if course not in courses:
        print(course, "- Invalid course")
        return

    if course in registered_courses:
        print(course, "- Duplicate registration")
        return

    details = courses[course]

    if details["prerequisite"] not in completed_courses:
        print(course, "- Missing prerequisite")
        return

    current_credits = sum(
        courses[c]["credits"] for c in registered_courses
    )

    if current_credits + details["credits"] > credit_limit:
        print(course, "- Credit limit exceeded")
        return

    for registered in registered_courses:
        if courses[registered]["time"] == details["time"]:
            print(course, "- Timetable conflict")
            return

    registered_courses.append(course)
    print(course, "- Registration successful")


print("Student ID:", student_id)
print("Semester:", semester)
print("Credit Limit:", credit_limit)
print()

for course in selected_courses:
    register_course(course)

print("\nRegistered Courses:")

total_credits = 0

for course in registered_courses:
    print(course, "-", courses[course]["credits"], "credits")
    total_credits += courses[course]["credits"]

print("Total Registered Credits:", total_credits)
