names = ["Asha", "Bala", "Charan", "Divya", "Esha"]
subjects = ["Maths", "Physics", "Chemistry", "English"]
marks = [[85, 78, 92, 70],
         [45, 38, 50, 62],
         [90, 88, 79, 85],
         [60, 55, 48, 72],
         [30, 42, 35, 58]]
low_avg_limit = 50

rows = len(marks)
cols = len(subjects)

print("Row-wise statistics")
best_total = -1
best_student = ""
for i in range(rows):
    total = 0
    for j in range(cols):
        total = total + marks[i][j]
    avg = total / cols
    print(names[i], "Total:", total, "Average:", avg)
    if total > best_total:
        best_total = total
        best_student = names[i]

print("\nColumn-wise statistics")
for j in range(cols):
    col_total = 0
    highest = marks[0][j]
    topper = names[0]
    for i in range(rows):
        col_total = col_total + marks[i][j]
        if marks[i][j] > highest:
            highest = marks[i][j]
            topper = names[i]
    col_avg = col_total / rows
    print(subjects[j], "Average:", col_avg, "| Topper:", topper, "(", highest, ")")
    if col_avg < low_avg_limit:
        print("   -> LOW AVERAGE subject")

print("\nOverall top performer:", best_student, "with total", best_total)
