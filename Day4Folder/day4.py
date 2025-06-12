# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
print("hello from day4")

# recap
# import random 

# for count in range(10):
#     randomnumber = random.randint(1, 1000)
#     print(randomnumber)

########################################################################
# Task 1:

counter = 0
while counter < 5:
    print(counter)
    counter = counter + 1

########################################################################
# Task 2:

question = "what do you call a deer with no eyes?"
hidden_answer = "no idea"
guess = input( question )
while guess != hidden_answer:
    print("wrong answer! try again...")
    guess = input( question )



########################################################################
# Additional exercises: