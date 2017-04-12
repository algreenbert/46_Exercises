def max(num_one, num_two):
    if num_one >= num_two:
        return num_one
    elif num_two > num_one:
        return num_two
    else:
        print "What did you do?"
        return num_one - num_two

print max(3, 5)

print max(7,7)
