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
