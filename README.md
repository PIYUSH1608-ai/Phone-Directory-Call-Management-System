# Phone Directory & Call Management System

An object-oriented Phone Directory and Call Management System developed using Python. The project simulates basic smartphone contact management and calling functionalities through a command-driven interface.

## Features

### 1. Contact Management

* Add new contacts.
* Update existing contact names.
* Delete contacts.
* Search contacts using phone numbers.
* Search contacts using names.
* Search contacts using multiple keywords.

### 2. Call Management

* Initiate outgoing calls.
* Receive incoming calls.
* Accept incoming calls.
* Terminate active calls.
* Handle busy-device scenarios.
* Maintain individual call histories.

### 3. Call History & Analytics

* Record call timestamps and durations.
* Classify calls as dialled, received, missed or rejected.
* Calculate the number of unique outgoing contacts.
* Calculate average call duration.
* Identify frequently contacted numbers.

## Technical Concepts

* Object-Oriented Programming (OOP)
* Classes and Objects
* Encapsulation
* Object Relationships
* Dictionaries and Lists
* Set Operations
* String Manipulation
* Command Parsing
* State Management

## Project Structure

```text
Phone-Directory-Call-Management-System/
│
├── phone_directory.py
├── COMMAND.txt
└── README.md
```

## How to Run

**Prerequisites:** Python 3.x

1. Clone the repository:

```bash
git clone https://github.com/PIYUSH1608-ai/Phone-Directory-Call-Management-System.git
```

2. Navigate to the project directory:

```bash
cd Phone-Directory-Call-Management-System
```

3. Run the simulation:

```bash
python phone_directory.py
```

The program reads commands from `COMMAND.txt` and executes the corresponding operations.

## Sample Commands

```text
CREATE_PHONE Alice 111
CREATE_PHONE Bob 222

ADD_CONTACT 111 Bob 222
ADD_CONTACT 222 Alice 111

CALL 111 222 100
ACCEPT 222 110
END 111 170
```

## Future Improvements

* Introduce a dedicated CallSession class.
* Improve call-state management using enumerations.
* Add persistent storage using a database.
* Implement a graphical user interface.
* Expand automated testing for edge cases.

## Project Purpose

This project was developed to explore object-oriented design, data structures, state management and the implementation of real-world entity relationships through a command-driven simulation.
