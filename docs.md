# Plagg - A Simple Voice Assistant

This Python script defines a simple voice assistant named Plagg. The assistant uses various modules to perform different tasks based on the user's voice commands.

## Modules

The script imports several modules, each responsible for a specific functionality:

- `datetime` and `time`: Standard Python modules for date and time operations.
- `tts_module`: A custom module for text-to-speech conversion.
- `weather_module`: A custom module for fetching weather updates.
- `news_module`: A custom module for fetching news.
- `time_module`: A custom module for getting the current time.
- `math_module`: A custom module for solving math problems.
- `wikipedia_module`: A custom module for fetching information from Wikipedia.
- `location_module`: A custom module for getting the current location.
- `dictionary_module`: A custom module for getting word definitions.
- `jokes_module`: A custom module for fetching jokes.
- `trivia_module`: A custom module for fetching trivia questions.
- `unit_conversion_module`: A custom module for converting units.
- `speech_recognition_module`: A custom module for speech recognition.

## Functions

The script defines two main functions:

- `greet_user()`: This function greets the user based on the current time of the day. It uses the `datetime` module to get the current time and then uses the `speak` function from the `tts_module` to greet the user.

- `main()`: This function contains the main logic of the voice assistant. It starts by greeting the user and then enters an infinite loop, waiting for the user's voice commands. The `get_user_input` function from the `speech_recognition_module` is used to capture the user's voice input. The voice assistant can perform various tasks such as providing weather updates, news, word definitions, jokes, trivia, unit conversions, current time, solving math problems, providing Wikipedia information, and current location. Each of these tasks is performed by a specific module and the corresponding function in that module is called based on the user's voice command.

## Execution

The script is executed from the command line. If the script is run as the main program (i.e., not imported as a module), the `main` function is called.
