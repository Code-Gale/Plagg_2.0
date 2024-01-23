import sympy as sp
from speech_recognition_module import get_user_input
from tts_module import speak


def solve_math_problem():
    # Ask the user for the math problem
    speak("Sure, what math problem would you like me to solve?")
    
    # Listen for user input
    user_input = get_user_input()

    # Use SymPy to solve the math problem
    x = sp.symbols('x')
    solution = sp.solve(user_input, x)
    return f"The solution is: {solution}"
