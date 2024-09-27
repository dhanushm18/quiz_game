from quiz_database import question_bank
from quiz_database import options


print("***********************")
print("Welcome to My Quiz Game!!!")


def check_answer(user_guess,correct_answer):
    if(user_guess==correct_answer):
        return True
    else:
        return False
score=0
for question_num in range(len(question_bank)):
    print("**********************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    
    user_guess=input("Enter the choice(A/B/C/D): ").upper()
    is_correct=check_answer(user_guess,question_bank[question_num]["answer"])
    if(is_correct):
        print("!!correct answer!!")
        score=score+1
    else:
        print("Incorrect Answer")
        print("The correct Answer is: ",question_bank[question_num]["answer"])

    print(f"Your Current score is {score}/{question_num+1}")
    print()
    print()

print(f"You have given  {score} correct answers")
print(f"Your is score is ",(score/len(question_bank))*100,"%")