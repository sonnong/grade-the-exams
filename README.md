# grade_the_exams

## About
A Python script to grade students' exams. It processes the student's answers data, displays a general statistical analysis and outputs the grades into a text file.

## Prerequisite
- Python 3 with _pandas_ library
- The input data must be a comma-delimited TXT file, each line represents
a student's answers to 25 questions (an answer can be blank) and includes
a student ID. Below is an example of a student who has all the correct answers:

    >N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D

## Usage
- The script must be placed at the same location of the data. It asks for input data first, simply enter the file name (without .TXT extension) then if found, general statistics and invalid data (if any) are displayed
- Output TXT file (for valid data) includes the student's ID and grade.

## License
Free to use. See the **UNLICENSE** file for more information.
