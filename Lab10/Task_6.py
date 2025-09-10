def grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"
print(grade(95))
print(grade(72))
print(grade(68))
print(grade(58))