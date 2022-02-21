from glob import escape
from tkinter import END
from tkinter.messagebox import YES


print("Welcome to this Quizz Game!")
right_answer = 0
wrong_answer = 0
question = ""

# Start
playing = input("Are you ready to start!!: ")

if playing.lower() != "yes":
    quit()
else:
    question = (input("Question what year is it currently?: "))
    if question == "2022":
        right_answer += 1
    else:
        wrong_answer += 1
    question = (input("How many fingers do you have on 1 hand?: "))
    if question == "5":
        right_answer += 1
    else:
        wrong_answer += 1
    question = (input("Is the earth flat?: "))
    if question == "no":
        right_answer += 1
    else:
        wrong_answer += 1
    question = (input(
        "Does america have the highest total military budget spending in the world?: "))
    if question == "yes":
        right_answer += 1
    else:
        wrong_answer += 1
#calculator & formulas
percent = right_answer/(right_answer + wrong_answer) * 100
percent_false = wrong_answer/(right_answer+wrong_answer)*100
# output
print("You have "+str(right_answer)+" answers " +
      "and " + str(wrong_answer) + " wrong answers")
print("Out of all the questions you had this much percentage right " +
      str(percent)+"% " + "and "+str(percent_false)+"% was wrong!")
