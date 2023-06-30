import random

file_path = 'Citizenship_test.txt'

with open(file_path, 'r') as file:
    contents = file.read()

text_file = contents.splitlines()
result = {}
key = ""
value = ""

for item in text_file:
    if '?' in item:
        key = item
        value = ""

    elif item == "":
        if key != "":
            result[key] = value
            key = ""
            value = ""
    else:
        value = value + item + "\n"
    
keys = list(result.keys())  # Convert dictionary keys to a list
question_counter = {key: 0 for key in keys}  # Initialize counter for each question

while True:
    user_input = input("******* press Enter for a question, or enter 'q' to quit *******")
    
    if user_input.lower() == 'q':
        break  # Exit the loop if 'q' is entered

    remaining_questions = [question for question in keys if question_counter[question] < 3]

    if not remaining_questions:
        print("---- All questions have been asked 3 times. Exiting ----")
        continue

    random_question = random.choice(remaining_questions)
    question_counter[random_question] += 1  # Increment question counter
    print("\nQuestion: \n{}\n".format(random_question))   


    input("******* Press Enter to get the answer *******")
    answer = result[random_question]
    print("\nAnswer: \n>>> {}---------------------------------------------------------------------------------------------------------------\n".format(answer))