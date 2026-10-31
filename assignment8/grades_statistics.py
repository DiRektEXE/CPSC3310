# Vajaran Nall

from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent /"grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, compute each student's weighted final
    grade, and print a summary of how many students fall into each
    grade range.

    # TODO - Read GRADES_FILE and build a list of each student's
    #        weighted final grade (skip the header row, and use
    #        process_row() to do the per-student work).
    # TODO - Pass that list to analyze_grade() to print the summary.
    # TODO - Use try/except to handle a missing file and any other
    #        errors that can occur while reading or processing it.
    """
    
    try:
        final_grades = []

        with GRADES_FILE.open('r', encoding='utf-8') as file:

            next(file)
            for row in file:
                if not row.strip():
                    continue

                final_grade = process_row(row)
                final_grades.append(final_grade)

        analyze_grade(final_grades)

    except FileNotFoundError:
        print("Error: The file containing grades was not found.")

    except ValueError:
        print("Error: File contains invalid grade value.")

    except IndexError:
        print("Error: Some row is missing at least one grade column.")



def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""
    # TODO - Implement this function.

    grades = row.strip().split(",")

    # Retrieve score and cast them to floating point values
    test_scores = [float(score) for score in grades[2:6]]
    exam_scores = [float(score) for score in grades[6:8]]
    discussion_scores = [float(score) for score in grades[8:10]]
    project_score = float(grades[10])

    # Averages
    test_avg = average_subject(test_scores)
    exam_avg = average_subject(exam_scores)
    discussion_avg = average_subject(discussion_scores)

    return weight_final(test_avg, exam_avg, discussion_avg, project_score)


def average_subject(subject_list):
    """Return the average of the scores in subject_list."""
    # TODO - Implement this function.
    return sum(subject_list) / len(subject_list)


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above."""
    # TODO - Implement this function.
    return (TEST_WEIGHT * test_avg + EXAM_WEIGHT * exam_avg + DISCUSSION_WEIGHT * discussion_avg + PROJECT_WEIGHT * project_score)


def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60."""
    # TODO - Implement this function.

    grade_counts = {
        "90 or above": 0,
        "80-89": 0,
        "70-79": 0,
        "60-69": 0,
        "below 60": 0
    }

    for grade in weight_final_list:

        if grade >= 90:
            grade_counts["90 or above"] += 1

        elif grade >= 80:
            grade_counts["80-89"] += 1

        elif grade >= 70:
            grade_counts["70-79"] += 1

        elif grade >= 60:
            grade_counts["60-69"] += 1

        else:
            grade_counts["below 60"] += 1

    for category, count in grade_counts.items():
        print(f"Number of students with final grade {category}: {count}")
    

if __name__ == "__main__":
    main()
