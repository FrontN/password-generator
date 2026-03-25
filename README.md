Python Password Generator 🔐
A robust, terminal-based security utility implemented in Python that generates high-entropy, customizable passwords with a professional CLI interface.

Features 🎮
Smart Sampling Logic: Uses random.choices (sampling with replacement) to allow password lengths that exceed the size of the character pools.

Robust Input Handling: Custom get_valid_int and get_valid_input functions ensure the program never crashes due to non-numeric or invalid entries.

Modular Architecture: Clean separation between input validation, generation logic, and UI rendering for maximum maintainability.

Dynamic Entropy: Combines three distinct character sets (Letters, Digits, and Punctuation) with a final random.shuffle to eliminate predictable patterns.

Polished UI: Features centered ASCII formatting and timed transitions (time.sleep) to provide a smooth, app-like experience in the console.

Password Logic 📋
The generator follows a structured assembly process to ensure maximum security:

Character Sourcing: Pulls from Python's official string module constants to guarantee a complete set of ASCII characters.

User Definition: The user specifies the exact count for each category:

Letters: (a-z, A-Z)

Numbers: (0-9)

Symbols: (!, #, $, %, etc.)

Shuffle Phase: Once the raw list is compiled, the algorithm shuffles the entire collection to ensure character types are not grouped together.

Formatting: Joins the list into a final string and displays it centered within a decorative border.

Project Structure 📁
Plaintext
password-generator/
├── main.py                                # Main logic and entry point
├── Password_generator_image.png           # Optional ASCII art assets
├── algoritmo_password.txt                 # Technical logic documentation
└── README.md                              # This file
Main Functions Overview:
clear_screen() - Clears the console based on the Operating System (Windows/Unix).

get_valid_int() - Traps ValueError exceptions to guarantee an integer is returned.

get_valid_input() - Normalizes and validates string choices (yes/no/y/n).

main() - Orchestrates the input collection, the lambda formula execution, and the replay loop.

Requirements ✅
Python 3.x

No external dependencies required (uses standard random, string, os, and time modules).

Installation & Setup 🚀
Clone the repository:

Bash
git clone https://github.com/FrontN/password-generator.git
cd password-generator
Run the generator:

Bash
python main.py
How to Use 🎯
Run the script and wait for the welcome message.

Enter the number of letters you want.

Enter the number of digits you want.

Enter the number of symbols you want.

Your secure password will be displayed inside a starred box.

Type y to generate another or n to exit.

Game Output Example 📺
Plaintext
****************************************
            Your password is            
        k9#L2!pQ8&m$Z1*Bv6^N            
****************************************

Do you want to generate another password? (yes/no):
Technical Highlights 💡
Lambda Functions: Uses a compact lambda formula to standardize the sampling process across different pools.

Safe Sampling: By using random.choices, the script avoids the ValueError that occurs in random.sample when the request size is larger than the pool.

Cross-Platform: The os.name check ensures the screen clears correctly on Windows, macOS, and Linux.

Future Enhancements 🎯
Strength Meter: Integration of an algorithm to rate the password as "Weak", "Medium", or "Strong".

Clipboard Support: Option to automatically copy the generated password to the system clipboard.

Secrets Module: Implementation of the secrets library for cryptographically strong, production-grade security.

Contributing 🤝
Feel free to fork this repository and submit pull requests for any improvements!

Author 👨‍💻
FrontN - Created as a project to master input validation and randomization logic in Python.
