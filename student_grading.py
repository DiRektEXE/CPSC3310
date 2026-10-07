"""calculate the student's grade based on the scores from the input and
the predefined weights for each category"""

def calculate_grade():

    # Weight scalar constants for each category
    EXAM_WEIGHT = 0.5
    ASSIGNMENT_WEIGHT = 0.3
    QUIZ_WEIGHT = 0.2

    # Acquire score values from the user as floats
    midterm_exam_grade = float(input("Please enter midterm grade: "))
    final_exam_grade = float(input("Please enter final exam grade: "))
    assignment_one = float(input("Please enter first assignment grade: "))
    assignment_two = float(input("Please enter second assignment grade: "))
    first_quiz = float(input("Please enter first quiz grade: "))
    second_quiz = float(input("Please enter second quiz grade: "))

    '''
    Calculate the average for each category and multiply by the weight scalar for that category
    if the user provided input falls within the approriate range
    '''    
    
    if((0 <= midterm_exam_grade <= 100) and (0 <= final_exam_grade <= 100)):
        exam_grade = ((midterm_exam_grade + final_exam_grade) / 2) * EXAM_WEIGHT
    else:
        print("Error: Exam Scores are out of range!")

    if ((0 <= assignment_one <= 30) and (0 <= assignment_two <= 30)):
        assignment_grade = ((assignment_one + assignment_two) / 2) * ASSIGNMENT_WEIGHT
    else:
        print("Error: Assignment Scores are out of range!")

    if ((0 <= first_quiz <= 20) and (0 <= second_quiz <= 20)):
        quiz_grade = ((first_quiz + second_quiz) / 2) * QUIZ_WEIGHT
    else:
        print("Error: Quiz Scores are out of range!")

    
    # Calculate the final grade by adding the weighted averages and dividing by 100
    final_grade = (exam_grade + assignment_grade + quiz_grade) / 100

    # Print the final grade with a floating point precision of 2 
    print(f"The students final grade is {final_grade:.2%}")

    if __name__ == "__main__":
        calculate_grade()