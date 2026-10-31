# Rules: max Rs10000 per withdrawal, max Rs20000 withdrawn per day,
# minimum balance Rs500 must remain, deposits must be positive

balance = 5000
per_txn_limit = 10000
daily_limit = 20000
min_balance = 500
withdrawn_today = 0

transactions = [("D", 2000), ("W", 3000), ("W", 12000), ("D", -500),
                ("W", 4500), ("X", 100), ("D", 15000), ("W", 9000), ("W", 9000)]

success = 0
rejected = 0
total_dep = 0
total_wd = 0

for t in transactions:
    kind, amount = t          # tuple unpacking
    if kind == "D":
        if amount > 0:
            balance = balance + amount
            total_dep = total_dep + amount
            success = success + 1
            print("Deposit", amount, "accepted. Balance:", balance)
        else:
            rejected = rejected + 1
            print("Deposit", amount, "REJECTED: invalid amount")
    elif kind == "W":
        if amount <= 0:
            rejected = rejected + 1
            print("Withdrawal", amount, "REJECTED: invalid amount")
        elif amount > per_txn_limit:
            rejected = rejected + 1
            print("Withdrawal", amount, "REJECTED: exceeds per-transaction limit")
        elif withdrawn_today + amount > daily_limit:
            rejected = rejected + 1
            print("Withdrawal", amount, "REJECTED: exceeds daily limit")
        elif balance - amount < min_balance:
            rejected = rejected + 1
            print("Withdrawal", amount, "REJECTED: insufficient balance")
        else:
            balance = balance - amount
            withdrawn_today = withdrawn_today + amount
            total_wd = total_wd + amount
            success = success + 1
            print("Withdrawal", amount, "accepted. Balance:", balance)
    else:
        rejected = rejected + 1
        print("Transaction type", kind, "REJECTED: unknown type")

print("\n--- Summary ---")
print("Successful:", success, " Rejected:", rejected)
print("Total deposited:", total_dep, " Total withdrawn:", total_wd)
print("Final balance:", balance)
