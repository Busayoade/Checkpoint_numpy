#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def calculate_grade(marks):
    # Define grading criteria or thresholds for different grades
    thresholds = [90, 80, 70, 60]
    grades = ['A', 'B', 'C', 'D', 'F']
    
    # Calculate total marks and percentage for each student
    total_marks = np.sum(marks, axis=1)
    percentage = (total_marks / marks.shape[1])  # Assuming equal weightage for all subjects
    
    # Calculate grades based on percentage
    student_grades = np.empty_like(percentage, dtype=str)
    for i, perc in enumerate(percentage):
        for j, threshold in enumerate(thresholds):
            if perc >= threshold:
                student_grades[i] = grades[j]
                break
        else:
            student_grades[i] = grades[-1]  # Assign 'F' grade for percentages below 60
    
    return total_marks, percentage, student_grades

# Get input from the user for number of students and subjects
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Create an empty array to store marks
marks_array = np.empty((num_students, num_subjects), dtype=int)

# Input marks for each student in each subject
for i in range(num_students):
    print(f"\nEnter marks for Student {i + 1}:")
    for j in range(num_subjects):
        marks_array[i][j] = int(input(f"Enter marks for Subject {j + 1}: "))

# Calculate total marks, percentage, and grades using the calculate_grade function
total_marks, percentage, student_grades = calculate_grade(marks_array)

# Display the results in a tabular format
print("\nStudent\t| Total Marks\t| Percentage\t| Grade")
print("-" * 45)
for i in range(num_students):
    print(f" {i + 1}\t| {total_marks[i]}\t\t| {percentage[i]:.2f}%\t\t| {student_grades[i]}")


# In[ ]:




