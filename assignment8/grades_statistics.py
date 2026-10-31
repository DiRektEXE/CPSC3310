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
    pass

def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""
    # TODO - Implement this function.
    pass

def average_subject(subject_list):
    """Return the average of the scores in subject_list."""
    # TODO - Implement this function.
    pass


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above."""
    # TODO - Implement this function.
    pass


def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60."""
    # TODO - Implement this function.
    pass

if __name__ == "__main__":
    main()
