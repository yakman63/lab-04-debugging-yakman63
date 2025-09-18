import sys

'''
Author: Matthew Remington
Date: September 15, 2025
Assignment: Lab 03
Course: CPSC 1051
Lab Section: 002

Calculates grades for CSPC 1050 and 1051.
'''
# --- SECTION 1: UNDERSTANDING THE SET UP

# --- SECTION 1.1: SETTING UP DEFAULT VALUES - NO BUGS HERE - DO NOT EDIT ---
print("Welcome to the Final Grade Calculator for CPSC 1050!")

min_points_for_letter = {
    "A": 894.5,
    "B": 794.5,
    "C": 694.5,
    "D": 594.5,
    "F": 0
}

assessments = {
    "Textbook Activities":      75,
    "Programming Assignments":  75,
    "In-Class Exercises":       100,
    "Quizzes":                  100,
    "Projects":                 150,
    "Labs":                     200,
    "Exam 1":                   100,
    "Exam 2":                   100
}

# --- SECTION 1.2: SETTING UP ASSESSMENT SCORES ---

for assessment, max_score in assessments.items():
    print(f"What is your {assessment} score out of {max_score}?")
    score = float(input())
    
    while 0 > score or score > max_score:
        print(f"Invalid score entry. Please enter a number between 0 and {max_score}.")
        score = float(input())
        
    assessments[assessment] = score


# --- SECTION 1.3: LAB ATTENDANCE ---

print("What is your lab attendance percentage out of 100?")
lab_attendance = float(input())

while lab_attendance < 0 or lab_attendance > 100:
    print("Invalid percentage entry. Please enter a percentage between 0 and 100.")
    lab_attendance = float(input())

drop_lowest_lab = False

if lab_attendance >= 90:
    drop_lowest_lab = True
elif lab_attendance < 50:
    print("\nUnfortunately, you have failed CPSC 1050:")
    print("\tYou must have at least 50% lab attendance to pass this course.")
    print(f"\tYour lab attendance is {lab_attendance}%.")
    print("Exiting calculator.")
    sys.exit()
    
    
# --- SECTION 1.4: DROPPING LOWEST LAB ---
if drop_lowest_lab:
    print(f"Congratulations! You have high enough lab attendance to drop your lowest lab grade!")
    print("What is your lowest lab grade out of 20? (Sum of Parts A, B, C)")
    
    lowest_lab = float(input())
    
    while not 0 <= lowest_lab <= 20:
        print(f"Invalid score entry. Please enter a number between 0 and 20.")
        lowest_lab = float(input())
    
    old_lab_score = assessments["Labs"]
    lab_score = 200 * (old_lab_score - lowest_lab) / 180
    assessments["Labs"] = lab_score
    
    print(f"Your lab score of {old_lab_score:.2f}/200 has been updated to {lab_score:.2f}/200.")       
 
    
# --- SECTION 1.5: LAB FAIL CONDITION ---
if assessments["Labs"]/2 < 59.5:
    print("\nUnfortunately, you have failed CPSC 1050:")
    print("\tYou must pass the lab section (60%+) to pass this course.")
    print(f"\tYour lab score is {assessments['Labs']:.2f}/200, or {assessments['Labs']/2:.2f}%.")
    print("Exiting calculator.")
    sys.exit()


# --- SECTION 1.6: TOTAL POINTS ---
total_points = 0
for assessment, score in assessments.items():
    total_points += score
    
print(f"Your total score is currently {total_points:.2f} out of 900, or {total_points/900*100:.2f}%.")


# --- SECTION 2: THE CALCULATOR ---

# --- SECTION 2.1: PROMPT FUNCTION - NO BUGS HERE - DO NOT EDIT ---
def prompt_options():
    print("\nPlease choose one of these options:")
    print("F - Calculate Final exam grade needed for a desired letter grade.")
    print("C - Calculate Course grade with a given final exam grade.")
    print("Q - Quit the program")    
    
    choice = input().strip().upper()
    while choice not in ["F","C","Q"]:
        print("Invalid choice. Please choose F, C, or Q.")
        choice = input().strip().upper()
    
    return choice


# --- SECTION 2.2: THE INTERACTION LOOP ---

running = True
choice = prompt_options()

while running:

    # --- SECTION 2.3: FINAL EXAM SCORE NEEDED FOR DESIRED LETTER GRADE ---
    if choice == "F":
        print("Enter your desired letter grade (A, B, C, D, F)")
        desired_letter = input().strip().upper()
        
        while desired_letter not in ["A","B","C","D","F"]:
            print("Invalid choice. Please choose A, B, C, D, or F.")
            desired_letter = input()

        lowest_score_for_letter = min_points_for_letter[desired_letter]
        
        lowest_final_for_desired_grade = lowest_score_for_letter - total_points     
        final_exam_score = lowest_final_for_desired_grade
        
        print(f"A letter grade of {desired_letter} requires {lowest_score_for_letter}/1000 points.")
        print(f"To achieve this, you must score at least {lowest_final_for_desired_grade:.2f} points on your final exam.")
        if lowest_final_for_desired_grade > 100:
            final_exam_score = 100
            print(f"This score is impossible. The maximum final exam grade is 100 points.")
        elif lowest_final_for_desired_grade < 0:
            final_exam_score = 0
            print(f"This score is impossible. The minimum final exam grade is 0 points.")
    

    # --- SECTION 2.4: PREDICT LETTER GRADE WITH GIVEN FINAL EXAM SCORE ---
    elif choice == "C":
        print("Enter your predicted final exam score:")
        predicted_final_score = float(input())
        final_exam_score = predicted_final_score
        
        while not 0 <= predicted_final_score <= 100:
            print("Invalid score entry. Please enter a score between 0 and 100.")
            predicted_final_score = float(input())
            final_exam_score = predicted_final_score
    
        total_w_final = total_points + predicted_final_score

        letter_grade = None
        for letter in ["A","B","C","D","F"]:
            if min_points_for_letter[letter] <= total_w_final:
                letter_grade = letter
                break
        
        print(f"With a final exam score of {predicted_final_score:.2f} your total course score would be {total_w_final:.2f}/1000.")
        print(f"This score would grant a letter grade of {letter_grade}.")
        
    
    # --- SECTION 2.5: EXAM FAIL CONDITION ---
    exam_average = (assessments["Exam 1"] + assessments["Exam 2"] + final_exam_score)/3

    if exam_average < 59.5 and choice != "Q":
        print("\nYou must have a passing exam average (60%+) to pass this course.")
        print(f"With a final exam score of {final_exam_score:.2f}, your exam average comes to {exam_average:.2f}.")
        print("Unfortunately, you have failed CPSC 1050.")
        print("Better luck next semester!")
    

    # --- SECTION 2.6: RESTART OR QUIT? ---
    if choice != "Q":
        choice = prompt_options()
    else:
        print("Quitting...")
        running = False