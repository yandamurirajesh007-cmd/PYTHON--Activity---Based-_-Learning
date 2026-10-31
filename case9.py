
shifts = [("Arun", "Mon", 9, 13),
          ("Arun", "Mon", 12, 17),
          ("Bhavya", "Mon", 9, 13),
          ("Bhavya", "Tue", 13, 18),
          ("Chetan", "Wed", 8, 12),
          ("Chetan", "Wed", 12, 16),
          ("Arun", "Tue", 10, 14),
          ("Chetan", "Wed", 11, 15)]

conflicting_employees = []

for i in range(len(shifts)):
    for j in range(i + 1, len(shifts)):
        emp1, day1, s1, e1 = shifts[i]    # tuple unpacking
        emp2, day2, s2, e2 = shifts[j]
        if emp1 == emp2 and day1 == day2:
            if s1 < e2 and s2 < e1:
                print("CONFLICT:", emp1, "on", day1, "->",
                      str(s1) + "-" + str(e1), "overlaps", str(s2) + "-" + str(e2))
                if emp1 not in conflicting_employees:
                    conflicting_employees.append(emp1)

print("\nEmployees with conflicting schedules:", conflicting_employees)
if len(conflicting_employees) == 0:
    print("No conflicts found")
