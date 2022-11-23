# GPA calc

all_grades = ["a", "a-", "b+", "b", "b-", "c+", "c", "c-", "d+", "d", "d-", "f"]
all_gpa = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0]

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
        letter_value = all_grades.index(grade)
        gpa_total += all_gpa[letter_value]
    return gpa_total / len(grades)
    
main()