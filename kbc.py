def questions(option_number):
    question_list = ['Who are you?','How are you?']
def answers(option_number):
    asnwer_list = ['Ronak','Good']
def check(question_list,answer_list,option_number):
    if (question_list[option_number]==answer_list[option_number]):
        print("Your answer is Correct! You have won $")
    else:
        pass
def game(question_list,answer_list,option_number):
    print("Welcome to the game! You have to answer the questions correctly to win the game!")
    print("You have 4 options to choose from! Good Luck!")
    for i in range(2):
        print(question_list[i])
    pass
