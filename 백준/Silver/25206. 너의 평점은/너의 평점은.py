score = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

grade_tot = 0
sub_tot = 0

for _ in range(20):
    sub, grade, rate = input().split()
    grade = float(grade)

    if rate in score:
        grade_tot += grade
        sub_tot += grade * score[rate]

result = sub_tot / grade_tot
print(f"{result:.6f}")