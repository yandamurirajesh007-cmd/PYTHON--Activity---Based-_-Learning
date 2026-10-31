# Slabs: first 100 units Rs3, next 100 Rs5, next 100 Rs7, above 300 Rs9
# Fixed charge Rs50, surcharge 10% of energy charge if units > 300
# Rebate Rs20 if units <= 100, unusual increase = more than 30% rise over previous month

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
units = [90, 135, 150, 260, 140, 320]
fixed_charge = 50
bills = []

print("Month  Units  Energy  Surcharge  Rebate  Total Bill")
for i in range(len(units)):
    u = units[i]
    if u <= 100:
        energy = u * 3
    elif u <= 200:
        energy = 300 + (u - 100) * 5
    elif u <= 300:
        energy = 300 + 500 + (u - 200) * 7
    else:
        energy = 300 + 500 + 700 + (u - 300) * 9

    surcharge = 0
    if u > 300:
        surcharge = 0.10 * energy

    rebate = 0
    if u <= 100:
        rebate = 20

    total = energy + fixed_charge + surcharge - rebate
    bills.append(total)
    print(months[i], "  ", u, "  ", energy, "  ", surcharge, "  ", rebate, "  ", round(total, 2))

print("\nMonth-to-month comparison")
for i in range(1, len(bills)):
    change = bills[i] - bills[i - 1]
    percent = change / bills[i - 1] * 100
    line = months[i - 1] + " -> " + months[i] + ": " + str(round(percent, 2)) + "%"
    if percent > 30:
        line = line + "  <-- UNUSUAL INCREASE"
    print(line)
