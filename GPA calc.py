# GPA calc

all_grades = ["a", "a-", "b+", "b", "b-", "c+", "c", "c-", "d+", "d", "d-", "f"]

def main():
    print("Welcome to GPA calc")
    n_classes = input("How many classes are you taking? : ")
    if n_classes.isdigit() == False:
        print("Please enter integer")
        main()
    ans = input("Begin calc? (y/n) ")
    if ans.lower() == "y":
        grade_list = grades(n_classes)
    elif ans.lower() == "n":
        main()
    else:
        main()
    final_gpa = calc(grade_list)
    print("Your GPA is: " + str(final_gpa))
    quit()

def grades(n_classes):
    grades = []
    while len(grades) < int(n_classes):
        g = input("Enter grade: ")
        if g.lower() in all_grades:
            grades.append(g)
        else:
            print("Please only type single letter grades")
            continue
    return grades


def calc(grades): 
    gpa_total = 0
    for grade in grades:
        if grade == "a":
            gpa_total += 4.0
        elif grade == "a-":
            gpa_total += 3.7
        elif grade == "b+":
            gpa_total += 3.3
        elif grade == "b":
            gpa_total += 3.0
        elif grade == "b-":
            gpa_total += 2.7
        elif grade == "c+":
            gpa_total += 2.3
        elif grade == "c":
            gpa_total += 2.0
        elif grade == "c-":
            gpa_total += 1.7
        elif grade == "d+":
            gpa_total += 1.3
        elif grade == "d":
            gpa_total += 1.0
        elif grade == "d-":
            gpa_total += 0.7
        else:
            gpa_total += 0
    return gpa_total / len(grades)
    
main()

print("Gabagool")