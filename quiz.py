answer = input("Who invented Computer: ")
if answer == "Charles Babbage":
    print("correct")
else:
    print(f"The answer is 'Charles Babbage', not {answer!r}")

answer = input("When was the first known use of the word 'quiz'? ")
if answer == "1781":
    print("Correct!")
else:
    print(f"The answer is '1781', not {answer!r}")

answer = input("Which built-in function can get information from the user? ")
if answer == "input":
    print("Correct!")
else:
    print(f"The answer is 'input', not {answer!r}")
    
QUESTIONS = [
    ("When was the first known use of the word 'quiz'", "1781"),
    ("Which built-in function can get information from the user", "input"),
    ("Which keyword do you use to loop over a given list of elements", "for")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")








