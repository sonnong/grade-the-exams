import pandas as pd
import re
try:
    # Open and read the data

    filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    with open(filename+'.txt', 'r') as class_file:
        class_data = class_file.readlines()
    print("Successfully opened {}.txt".format(filename))

    # Validate the data

    print("\n**** ANALYZING ****\n")
    valid_data = class_data[:]
    for line in class_data:
        answer_list = line.split(',')
        stuID = answer_list[0]
        if len(answer_list) != 26:
            print("Invalid line of data: does not contain exactly 26 values:", line)
            valid_data.remove(line)
        if not re.fullmatch('N[0-9]{8}', stuID):
            print("Invalid line of data: N# is invalid", line)
            valid_data.remove(line)
    if len(class_data) == len(valid_data):
        print("No errors found!")
    print("\n**** REPORT ****\n")
    print("Total valid lines of data:", len(valid_data))
    print("Total invalid lines of data:", len(class_data) - len(valid_data))

    # Statistical analysis

    answer_key = ['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','D','D']

    def grade(line):    # A function to calculate grade for each student
        score = 0
        for i in range(25):
            if line[i] == answer_key[i]:
                score += 4
            elif line[i] != '':
                score -= 1
        return score

    class_df = pd.DataFrame(data=[line.strip().split(',') for line in valid_data], columns=['ID']+[x for x in range(1, 26)]).set_index('ID')
    class_df['grade'] = class_df.apply(grade, axis=1, raw=True)
    print("\nMean (average) score:", round(class_df['grade'].mean(), 2))
    print("Highest score:", class_df['grade'].max())
    print("Lowest score:", class_df['grade'].min())
    print("Range of scores:", class_df['grade'].max() - class_df['grade'].min())
    print("Median score:", class_df['grade'].median())

    # Output the result to a text file

    class_df.to_csv(filename+'_grades.txt', columns=['grade'], header=False)

except:
    print("File cannot be found.")
