# -*- coding: utf-8 -*-
import os

# task 1
folder_path = "C:/Users/karin/OneDrive/Desktop/studying/python/Lab1/student_marks"
required_files = ["math.txt", "physics.txt", "statistics.txt", "student_names.txt"]
data = {}

available_files = os.listdir(folder_path)

for file in required_files:
    if file in available_files:
        file_path = os.path.join(folder_path, file)
        print(f"Reading file: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            data[file.replace(".txt", "")] = f.read().splitlines()  
    else:
        print(f"Error: File {file} not found in {folder_path}.")
        exit()

for key, value in data.items():
    print(f"Data from {key}: {value}")

# task 2
'''
students = data["student_names"]

def convert_to_int_list(score_list, subject):
    try:
        return list(map(int, score_list))
    except ValueError:
        print(f"Error: Invalid data format in {subject}. Ensure all scores are integers.")
        exit()

math_scores = convert_to_int_list(data["math"], "math")
physics_scores = convert_to_int_list(data["physics"], "physics")
statistics_scores = convert_to_int_list(data["statistics"], "statistics")

student_data = {}
for i, student in enumerate(students):
    student_data[student] = {
        "math": math_scores[i],
        "physics": physics_scores[i],
        "statistics": statistics_scores[i],
    }

print("Processed student data:")
for student, scores in student_data.items():
    print(f"{student}: {scores}")
'''

# task 3
'''
print("\nAverage scores of students:")
students_average_scores = {}
for student, scores in student_data.items():
    average_score = sum(scores.values()) / len(scores)
    students_average_scores[student] = average_score
    print(f"Student: {student}, Average Score: {average_score:.2f}")

print("\nTop three students with the highest average scores:")
top_students = sorted(students_average_scores.items(), key=lambda x: x[1], reverse=True)[:3]
for i, (student, average_score) in enumerate(top_students, start=1):
    print(f"Student {i}: {student}, Average Score: {average_score:.2f}")

print("\nOverall Statistics:")
num_students = len(student_data)
subject_statistics = {"math": [], "physics": [], "statistics": []}

for scores in student_data.values():
    for subject, score in scores.items():
        subject_statistics[subject].append(score)


print(f"Total number of students: {num_students}")
for subject, scores in subject_statistics.items():
    avg_score = sum(scores) / len(scores)
    min_score = min(scores)
    max_score = max(scores)
    print(f"{subject.capitalize()}: Average Score: {avg_score:.2f}, Min Score: {min_score}, Max Score: {max_score}")


print("\nStudents with the highest scores in each subject:")
for subject in subject_statistics:
    max_score = max(subject_statistics[subject])
    top_student = next(student for student, scores in student_data.items() if scores[subject] == max_score)
    print(f"{subject.capitalize()}: {top_student}, Score: {max_score}")
    

print("\nStudents with an average score below 50:")
low_score_students = [student for student, avg in students_average_scores.items() if avg < 50]
print(f"Number of students with an average score below 50: {len(low_score_students)}")
for student in low_score_students:
    print(student)
'''