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
