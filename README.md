
TDD System Project

📌 Overview

This project is a Test-Driven Development (TDD) System for a String Calculator built in Python. The implementation follows TDD principles, starting with the simplest test cases and iteratively improving the solution.

🛠 Features

Handles an unknown number of numbers separated by commas or new lines.

Supports custom delimiters (single and multiple characters).

Ignores numbers greater than 1000.

Throws an exception for negative numbers.

Developed using Python's unittest framework.

🚀 Installation

Clone the repository:

git clone https://github.com/Shivam-Chauhan/TDD-System-Project.git
cd TDD-System-Project

Set up a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

📝 Usage

Run the string calculator directly in Python:

from tdd_main import StringCalculator

calc = StringCalculator()
result = calc.add("1,2,3")
print(result)  # Output: 6

🧪 Running Tests

Run unit tests using:

python -m unittest discover tdd_test

TDD-System-Project/
│── tdd_main.py         # String Calculator implementation
│── tdd_test/           # Test directory
│   ├── tdd_test1.py    # Unit tests
│── README.md           # Project documentation
│── .gitignore          # Ignored files
