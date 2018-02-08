# f = open("questions.txt")
# lines = f.read()
# f.close()
# print(lines)

def show_menu():
    print('1. Ask Questions')
    print('2. Add a Questions')
    print('3. Exit')
    
    option = input('Enter your choice: ')
    return int(option)
    
def ask_questions():
    with open('questions.txt', 'r') as f:
        lines = f.read().split('\n')
    
def add_a_question():
    question = input('Enter a question: ')
    answer = input('OK, tell me the answer: ')
    with open('questions.txt', 'a') as f:
        f.write(question + '\n')
        f.write(answer + '\n')
    # Write the qa to the file
    
def game_loop():
    while True:
        option = show_menu()
        if option == 1:
            ask_questions()
        if option == 2:
            add_a_question()
        if option == 3:
            break
    
game_loop()