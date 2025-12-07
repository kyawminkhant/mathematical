# mathematical
Mathematical program that can be used in daily basis
------------------------------

🧮 Python Equation Solver
A custom-built equation interpreter written in Python that can evaluate complex mathematical expressions without using built-in functions like eval().
This program supports:
√ Multi-digit numbers
√ Decimal values
√ Nested parentheses
√ Standard operator precedence
√ Exponentiation, multiplication, division, addition, and subtraction (Follows BODMAS)

------------------------------

✨ Features
✔ Tokenizes user input safely
✔ Validates expression structure
✔ Recursively evaluates brackets
✔ Handles operator precedence:

------------------------------

Priority	Operator	Type
1.	^	Power
2.	*, /	Multiplication / Division
3.	+, -	Addition / Subtraction

------------------------------

✔ Works with expressions such as:
(((13+14)/3)+2)
2^3+4*(6/3)-1
(3+5)*(2+6)/4

------------------------------

▶️ Example Use
Enter the equation: ((13+14)/3)+2
The result of the equation is 11.0

------------------------------

Another example:
Enter the equation: 2^3 + 4 * (6/3) - 1
The result of the equation is 11.0

------------------------------

📂 File
File	             |  Purpose
equation_solver.py |	Main logic for parsing and solving expressions

------------------------------

🔧 Requirements
Python 3.8+
No external libraries required

------------------------------

🚀 Future Improvements
» Negative number handling (-5+3)
» Advanced functions: sin(), sqrt(), log(), etc.
» GUI interface (Tkinter or PyQt)
» Full calculator mode (history, memory, clear, etc.)

------------------------------

📜 License
MIT License — free to use, modify, and improve.

------------------------------

👨‍💻 Author
Created by Kyaw Min Khant as a project to practice parsing logic, recursion, and algorithm-based expression evaluation.
