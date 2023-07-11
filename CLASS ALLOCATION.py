"""Section 3: Python Challenge  [25 marks]
You are tasked with calculating the minimum classes we need to have so we know how many people to employ. Write a function which when given a number of students, calculates and prints out a string for your proposed number of classes, and a dictionary showing the allocation. 
Key Constraints:
The maximum size of a class is 30
There needs to be a minimum of 2 classes
The distribution of each class should be as even as possible. 
We want to hire as little people as possible - so where possible focus on bigger classes, and less of them!
Inputs/Outputs:
If 31 was the input, the output would be:
Proposed Allocation: 2 classes
{'Class 1': 16, 'Class 2': 15}

If 59 was the input, the output would be:
Proposed Allocation: 2 classes
{'Class 1': 30, 'Class 2': 29}

If 87 was the input, the output would be:
Proposed Allocation: 3 classes
{'Class 1': 29, 'Class 2': 29, 'Class 3': 29}
"""
def classAllocation(numStudents):
    numClasses = max(2, (numStudents + 29) // 30)  # calculates the minimum number of classes by adding 29 which ensure that when completing the floor division rounds up
    studentsClass = numStudents // numClasses  # calculate the number of students per class by diving the number of students by the number of classes
    remaining = numStudents % numClasses  # calculate the remaining students after equal distributing by number of students MOD number of classes

    allocation = {}  #  create dictionary in order to store the class allocation

    for i in range(1, numClasses + 1): 
        if i <= remaining: # checks if i is less than or equal to the remaining students
            allocation[f'Class {i}'] = studentsClass + 1 # if this is true then an exyra students should be added to one of the classes
        else:
            allocation[f'Class {i}'] = studentsClass # otherwise each of the classes should have the same amount of studnets 

    print(f"Proposed Allocation: {numClasses} classes") # displays the proposed allocarion of classes and  number of students in each class 
    print(allocation, "\n")# displays the allocation dictionary and line break  

# Examples given to test in question 
classAllocation(31)
classAllocation(59)
classAllocation(87)

