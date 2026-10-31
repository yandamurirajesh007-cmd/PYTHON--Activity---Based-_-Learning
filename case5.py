


key = "ABCDABCDAB"
students = [("Ravi", "ABCDABCDAB"),
            ("Sita", "ABC-ABDDA-"),
            ("Kiran", "DCBADCBADC"),
            ("Anu", "ABCDAB----")]
correct_mark = 4
negative_mark = 1

print("Name    Correct  Wrong  Unanswered  Score")
for s in students:
    name, answers = s          # tuple unpacking
    correct = 0
    wrong = 0
    blank = 0
    for i in range(len(key)):
        if answers[i] == "-":
            blank = blank + 1
        elif answers[i] == key[i]:
            correct = correct + 1
        else:
            wrong = wrong + 1
    score = correct * correct_mark - wrong * negative_mark
    print(name, "   ", correct, "   ", wrong, "   ", blank, "   ", score)
