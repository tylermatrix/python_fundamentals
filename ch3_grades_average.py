#Class average, sequence controlled repetition

total = 0
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82 94]

#processing
for grade in grades:
    total += grade #add current grades to the running total
    grade_counter += 1# indicate that more than one grade was processed


#termination phase
average = total / grade_counter
print(f"Class average is {average}")
