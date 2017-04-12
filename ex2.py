def max_of_three(num_one, num_two, num_three):
    # returns the biggest of three numbers
    if num_one >= num_two and num_one >= num_three:
        return num_one
    elif num_two >= num_three:
        return num_two
    else:
        return num_three

print max_of_three(1,1,2)
print max_of_three(1,3,1)
print max_of_three(4,1,1)
