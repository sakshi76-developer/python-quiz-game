questions = [
    {
        "questions": "What is the correct file extension for Python files?",
        "options": ["A. .pt", "B. .python", "C. .py", "D. .pyt"],
        "answers": "C"
    },
    {
        "questions": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answers": "C"
    },
    {
        "questions": "What will print(type(10)) output?",
        "options": ["A. <class 'float'>", "B. <class 'int'>", "C. <class 'str'>", "D. <class 'number'>"],
        "answers": "B"
    },
    {
        "questions": "Which data type is used to store multiple items in a single variable and is ordered?",
        "options": ["A. Set", "B. Dictionary", "C. Tuple", "D. List"],
        "answers": "D"
    },
    {
        "questions": "Which loop is used to iterate over a sequence in Python?",
        "options": ["A. repeat loop", "B. foreach loop", "C. for loop", "D. iterate loop"],
        "answers": "C"
    }
]


score = 0

print("---Welcome To The Quiz Game---")

for i,q in enumerate(questions,start=1):
    print(f"\nQuestions {i}: {q['questions']} ")

    for option in q["options"]:
        print(option)

    try:
            user_answer = input("Enter your answer (A/B/C/D)->").upper()

            if user_answer == q["answers"]:
                print("Correct Answer")
                score+=1

            else:
                print("Incorrect Answer")
                print("Correct answer is :",q["answers"])

    except Exception as e:
            print("Invalid answer",e)

print("\n Quiz Finished")
print("Your final Score :" ,score , "/" , len(questions))

percentage = (score / len(questions)) * 100
print("\n Percentaqe :",percentage , "%")

if percentage >= 80:
    print("Excellent Performance")
elif percentage >= 50:
    print("Good job")
else:
    print("Better luck next time")
    
