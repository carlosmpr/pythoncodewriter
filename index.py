import pyautogui
import time

def type_code(code, delay_between_keys=0.05):
    """
    Types the given code into the currently focused window, simulating keyboard presses.

    Args:
    - code: The string of code to type.
    - delay_between_keys: The delay (in seconds) between individual key presses.
    """
    for char in code:
        pyautogui.typewrite(char, interval=delay_between_keys)

# Example code
code_to_type ="""
import React from 'react';

const Greeting = ({ name }) => {
  return (
    <div className="max-w-md mx-auto mt-10 bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700">
        <div className="p-5">
            <h2 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Hello, {name}!</h2>
            <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">Welcome to our React component styled with Tailwind CSS.</p>
            <button className="inline-flex items-center py-2 px-3 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Say Hi
            </button>
        </div>
    </div>
  );
};

export default Greeting;

"""


# Wait a few seconds to manually focus on the text editor window
print("Switch to your text editor within 5 seconds...")
time.sleep(5)

# Type the code
type_code(code_to_type)
