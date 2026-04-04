# AgniVeer Recruitment System

## Project Overview
The AgniVeer Recruitment Database System is a sophisticated software solution designed to streamline the army recruitment process using Python and MySQL.

## Features
- User-friendly interface for recruiters and recruits
- Separate login systems for officers and recruits
- Candidate data management (personal details, medical records, qualifications)
- Advanced search and filtering capabilities
- Add, update, delete, and view recruit profiles
- Generate summary reports of all recruits

## Hardware Requirements
- CPU: Intel i3 2nd Gen or Higher / Ryzen 3 or Higher
- RAM: 2GB or Higher

## Software Requirements
- OS: Windows 7 or Higher / Apple OS
- Python: 3.7.9 or Higher
- MySQL: Latest version
- PIP: Package manager for Python libraries

## Installation Steps

### 1. Install Python
Download Python 3.7.9 or higher from https://www.python.org/downloads/

### 2. Install MySQL
Download and install MySQL from https://www.mysql.com/downloads/

### 3. Install Required Python Libraries
Open Command Prompt and run:
```bash
pip install mysql-connector-python
```

### 4. Create Database
1. Open MySQL Command Line Client or MySQL Workbench
2. Run the SQL commands from `AgniVeer_Database.sql` file
3. Or copy and paste the entire script in MySQL:
```bash
mysql -u root -p < AgniVeer_Database.sql
```

### 5. Update Database Credentials
Before running the application, update the database connection credentials in all Python files:
- In `signupgui.py`, `logingui.py`: Update host, user, and password according to your MySQL setup

Example:
```python
mydb = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='AgniVeer'
)
```

### 6. Run the Application
Navigate to the project directory and run:
```bash
python mainportalgui.py
```

## File Structure
```
AgniVeer-Recruitment-System/
├── mainportalgui.py          # Main portal interface
├── signupgui.py              # Signup module for recruits and officers
├── logingui.py               # Login module for recruits and officers
├── AgniVeer_Database.sql     # Database creation script
└── README.md                 # This file
```

## Usage Guide

### For Recruits:
1. Click "SIGN UP" to create a new account
2. Enter your name, email, and password
3. Click "LOGIN" to access your profile
4. View, edit your profile as needed

### For Officers:
1. Click "SIGN UP" → "OFFICER's SIGNUP"
2. Enter your credentials and secret code (default: "war")
3. Login with your credentials
4. Access features like:
   - Add a recruit
   - View all recruits summary
   - Find recruit profiles
   - Delete recruit profiles
   - Update recruit information

## Database Tables

### recruitdata
- id (Primary Key)
- name
- age
- qualification
- height
- address
- weight
- percentage

### recruitlogincred
- id (Primary Key)
- name
- mail
- pwd

### officerlogincred
- id (Primary Key)
- name
- mail
- pwd

## Limitations
1. System capabilities are limited to programmed features
2. Effectiveness depends on accuracy and completeness of data entered
3. No built-in data validation for medical records

## Future Enhancements
1. Add interview scheduling feature
2. Implement document upload functionality
3. Enable in-program notifications
4. Add email notifications
5. Implement role-based access control
6. Add data backup and recovery features

## Technologies Used
- Python (Tkinter for GUI)
- MySQL Database
- mysql-connector-python

## References
- Computer Science with Python by Priti Arora
- Computer Science with Python by Sumita Arora
- Geeks for Geeks
- YouTube Tutorials

## Author
Development Team - AgniVeer Project

## License
This project is for educational purposes.

## Support
For any issues or queries, please refer to the documentation or contact the development team.

---
**Note:** Update the database credentials (host, user, password) before running the application according to your MySQL setup.
