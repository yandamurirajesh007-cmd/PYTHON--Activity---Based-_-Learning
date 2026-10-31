

passwords = ["Hello@123", "password1", "ABC12", "Aaa@1234x", "Admin#2024", "Strong$Pass9"]
specials = "!@#$%^&*"
prohibited = ["password", "admin", "1234", "qwerty"]

for p in passwords:
    errors = []
    if len(p) < 8:
        errors.append("Length is less than 8 characters")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in p:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in specials:
            has_special = True

    if not has_upper:
        errors.append("Missing uppercase letter")
    if not has_lower:
        errors.append("Missing lowercase letter")
    if not has_digit:
        errors.append("Missing digit")
    if not has_special:
        errors.append("Missing special character (!@#$%^&*)")

    for i in range(len(p) - 2):
        if p[i] == p[i + 1] and p[i + 1] == p[i + 2]:
            errors.append("Character '" + p[i] + "' repeats 3 times consecutively")
            break

    for word in prohibited:
        if word in p.lower():
            errors.append("Contains prohibited substring '" + word + "'")

    print("Password:", p)
    if len(errors) == 0:
        print("  VALID")
    else:
        print("  INVALID")
        for e in errors:
            print("   -", e)
