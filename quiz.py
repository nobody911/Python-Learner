# Python quiz game

questions = ("Which animal lays the largest eggs?", 
             "Which element is abundant in the earth's atmosphere?",
             "How many bones are there in the human body?",
             "Which planet in our solar system is coldest?",
             "How many elements are there in the periodic table?")

options = (("A) Whale","B) Ostrich","C) Kiwi","D) Peacock"),
           ("A) Oxygen","B) Helium","C) Hydrogen","D) Nitrogen"),
           ("A) 206","B) 207","C) 200","D) 306"),
           ("A) Mercury","B) Uranus","C) Jupiter","D) Pluto"),
           ("A) 118", "B) 111", "C) 119", "D) 110"))

answers = ("B","D","A","D","A")
guesses = []
score = 0
question_num = 0

for question in questions:  
    print("------------------")
    print(question)

    for option in options[question_num]:
        print(option)
    usr_guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(usr_guess)

    if usr_guess == answers[question_num]:
        print("CORRECT!!!")
        score += 1
    else:
        print("INCORRECT!!!")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1

print()

print("-----------RESULT-------------")

print()

print("Your guesses -> ", end = "")
for guess in guesses:
    print(guess, end = " ")

print()

print("The answers -> ", end = "")
for answer in answers:
    print(answer, end = " ")

print()

score = int((score/len(questions))*100)
print(f"Your score is: {score}%")