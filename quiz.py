quiz = {
    "question1": {
        "question": "How many times did Naruto fail the graduation test from the Academy?",
        "answer": "Three"
    },
    "question2": {
        "question": "What jutsu is Naruto most proficient in?",
        "answer": "Shadow Clone"
    },
    "question3": {
        "question": "Name the legendary Sannin who became the fifth Hokage.",
        "answer": "Tsunade"
    },
    "question4": {
        "question": "Who secretly liked Naruto?",
        "answer": "Hinata"
    },
    "question5": {
        "question": "To whom does Naruto call Bushy Brow?",
        "answer": "Rock Lee"
    },    
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")

    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))
        print("")

print("You got " + str(score) + " out of 5 questions correctly")
print("")
print("Your percentage is " + str(score/5 * 100) + "%")