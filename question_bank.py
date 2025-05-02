#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for Salt?", "Nacl"),
        ("What is the chemical symbol for sulphuric acid?", "H2SO4"),
        ("What is the chemical symbol for Hydrogen?", "H2")
        # Add more questions as tuples (question, answer)
    ],
    "Math": [
    ("What is the square root of 144?", "12"),
    ("What is 7 x 8?", "56"),
    ("What is the value of π (up to 2 decimal places)?", "3.14")
]

}

hints = {
    "Science": [("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for Salt?", "Nacl"),
        ("What is the chemical symbol for sulphuric acid?", "H2SO4"),
        ("What is the chemical symbol for Hydrogen?", "H2")
        # Pair each question with a corresponding hint.
    ],
    "Math": [
    ("What is the square root of 144?", "12"),
    ("What is 7 x 8?", "56"),
    ("What is the value of π (up to 2 decimal places)?", "3.14")
]
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    L=questions[category]
    for i in L:
        if i[0]==question:
            L.remove(i)
            questions[category]=L
            break
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    print(question)
    ans=input("Give your answer: ")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    
    L=questions[category]
    for i in L:
        if i[0]==question:
            return i[1]    
    
    #------------------------
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    #------------------------

#---------------------------------------




