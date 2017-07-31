#by Juri Ahn
#Introduction commentary & selecting difficulty
print "Hello! Let's take a quiz!"
print "In this quiz, we will find out how much you know about StarCraft 2!"
print "First, choose a difficulty level by typing in Beginner, Intermediate, or Expert"
print "Remember, keep in mind singular or plural cues as well as capitalization!"



#I will give 4 blank spaces for each difficulty
blankSpaces = ["__1__", "__2__","__3__","__4__"]

#Below, are three different quizzes; one for each Beginner, Intermediate, and Expert
#Each quiz will ask questions varying in simplicity/complexity according to their difficulty

#Beginner quiz below
beginnerQuiz = "So you're a beginner to StarCraft 2! If you know ANYTHING about StarCraft, you know there are __1__ \n" \
               "races to choose from! There are the Terrans, __2__, and Zergs! For this game, you need to collect\n" \
               "resources called __3__ and Vespene Gas in order to create units or buildings. Lastly, you should \n" \
               "constantly scout the enemy team to detect any __4__ on your base and to prevent losing critical units early game!!\n"

#Answers for beginner quiz
beginnerQuizAnswers = ["3", "Protoss", "Minerals", "attacks"]

#Intermediate quiz
intermediateQuiz = "Okay, so you know a bit about StarCraft! If you're familiar with the three races, you should already \n" \
                   "know that the Protoss' Nexus costs __1__ minerals to build. If you know that your opponent is a \n" \
                   "Zerg, you better scout early to make sure they don't send any __2__ your way to attack your base! Also look \n" \
                   "out for their scouting units called __3__ so your build doesn't get discovered! If you're a Terran, always save \n" \
                   "energy for __4__ to detect any attacks from invisible units."

#Answers for intermediate quiz
intermediateQuizAnswers = ["400", "Zerglings", "Overlords", "scans"]

#Expert quiz
expertQuiz = "If you know StarCraft like the back of your hand, you shouldn't have a problem with this quiz, right? Being the expert that \n" \
             " you are, you know that micro-ing is extremely important for early game battles, when your army is smaller. __1__ step is an \n" \
             "extremely useful and effective tactic against non-ranged enemies. While you're meticulously managing your battles, you should \n" \
             "always keep track of unit upgrades. The Protoss uses the __2__ for core ground unit upgrades as well as the Twilight Council. If \n" \
             "you're a heavy stalker user, __3__ is an essential upgrade that is a must! Always keep track of enemy units going in, out, or even around\n" \
             "your base! Sometimes, a sneaky Zerg player will drop a __4__ worm in the corner of your base for an attack coming from the inside!\n"

#Answers for expert quiz
expertQuizAnswers = ["Stutter","forge", "blink", "nydus"]

def printLinesAboveAndUnder(lines):
    print "________________________________________________________________________________________________________________________________________________"
    print lines
    print "________________________________________________________________________________________________________________________________________________"

#this function will pass in the quiz with user input and return/replace answers
def start_quiz(quiz, answers):
    printLinesAboveAndUnder(quiz)
    var_quiz = quiz
    first_user_answer = raw_input("What is the first answer? ")
    var_quiz = checkAnswers(first_user_answer, answers[0], var_quiz, blankSpaces[0])
    second_user_answer = raw_input("What is the second answer? ")
    var_quiz = checkAnswers(second_user_answer, answers[1], var_quiz, blankSpaces[1])
    third_user_answer = raw_input("What is the third answer? ")
    var_quiz = checkAnswers(third_user_answer, answers[2], var_quiz, blankSpaces[2])
    fourth_user_answer = raw_input("What is the fourth answer? ")
    checkAnswers(fourth_user_answer, answers[3], var_quiz, blankSpaces[3])

#this function checks the user inputs to see if it matches up with the actual answers listed below each quiz//this function also replaces the inputs for the function above
def checkAnswers(userAnswer, actualAnswer, quiz, blankSpace):
    if userAnswer.lower() == actualAnswer.lower():
        newQuiz = quiz.replace(blankSpace, actualAnswer)
        printLinesAboveAndUnder(newQuiz)
        print "Great Job!"
        return newQuiz
    else:
        user_input_again = raw_input("Nope! Try again!")
        checkAnswers(user_input_again, actualAnswer, quiz, blankSpace)



#this function will aknowledge user choice in difficulty//the answers will also accept lowercased answers for user experience
def chooseDifficulty(levelOfDifficulty):
    if levelOfDifficulty.lower() ==  "Beginner".lower():
        start_quiz(beginnerQuiz,beginnerQuizAnswers)
    elif levelOfDifficulty.lower() == "Intermediate".lower():
        start_quiz(intermediateQuiz, intermediateQuizAnswers)
    elif levelOfDifficulty.lower() == "Expert".lower():
        #expert == Expert
        start_quiz(expertQuiz, expertQuizAnswers)
    else:
        print "Invalid input, try again!"
        user_input_difficulty = raw_input("Enter Difficulty Level : ")
        chooseDifficulty(user_input_difficulty)

#this will allow me to simulate the quiz to easily identify mistakes and to experience for myself what the user will be experiencing
user_input_difficulty = raw_input("Enter Difficulty Level : ")
chooseDifficulty(user_input_difficulty)

