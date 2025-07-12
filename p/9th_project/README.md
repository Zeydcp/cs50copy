# Bank Account
#### Video Demo:  <https://www.youtube.com/watch?v=cmRvsaMcsXA>
#### Description:

##### Bank Account Simulation

The "Bank Account" project is a Python-based simulation of an online banking platform, developed as the final project for CS50p. It offers users the ability to create accounts, log in securely, manage account balances, and perform basic financial transactions. The project is organized into three main files: project.py, registered.csv, and test_project.py, each playing a crucial role in the functionality of the simulation.

##### User Interaction

This bank account simulation is designed to interact with users through a command-line interface. Upon running project.py, users are presented with a simple table using the tabulate library. They have two primary options: to log in with an existing account or to register a new one. If any value other than these options is entered, the program raises a ValueError.

##### User Registration

When choosing to register a new account, users are prompted to enter a username and password. The system performs several checks to ensure data integrity. It verifies that the username consists of alphanumeric letters only, and the password is free from any whitespace. Additionally, it confirms that the chosen username is unique by checking against existing accounts stored in the registered.csv file.

##### Data Storage and Security

User account information is stored in a CSV file named registered.csv, featuring three essential columns: user, balance, and password. When a new account is created, the balance is initialized to 100, and the password is securely encrypted using the werkzeug.security library functions. This ensures the security and privacy of user data.

##### Account Management

Upon successful login, users are presented with three main choices: they can add cash to their account balance, withdraw cash, or log out. The program keeps track of user actions and updates the account balance accordingly. This project effectively demonstrates how to manage user data securely, perform authentication, and handle financial transactions within a command-line interface.

##### Technology Stack

The project is built using Python, with several libraries used for specific functionalities. These libraries include re, tabulate, csv, werkzeug.security, and pandas. These libraries collectively enable data validation, data presentation, secure password management, and efficient data manipulation.

##### Testing

To ensure the correctness and robustness of the code, the project includes a testing suite in test_project.py. This suite covers all functions used in the main program, testing them with various inputs and verifying the expected outcomes. Tests also predict and handle potential ValueError exceptions. The test suite can be run using pytest.

##### Challenges and Future Development

During development, one notable challenge was encountered while trying to modify the balance values in the CSV file using the CSV module. This issue was ultimately resolved by switching to the Pandas library, which offers more robust and user-friendly data handling capabilities. In the future, the project could be expanded by adding a deregistration mechanism, allowing users to delete their accounts securely.

##### Acknowledgments

The creator of this project would like to express their gratitude to God for unwavering support throughout this endeavor. Additionally, they would like to thank David Malan for his inspirational lectures in the CS50p course, which played a pivotal role in the successful completion of this project.