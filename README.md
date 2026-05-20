# Secure Coding Review using VS Code
## Project Screenshot

![Screenshot](code.png)

## Overview

This project demonstrates a basic Secure Coding Review using Python in Visual Studio Code (VS Code). The application contains a simple login system that is analyzed for common security vulnerabilities such as hardcoded passwords, weak authentication, and insecure coding practices.

The project also uses the **Bandit** security analysis tool to identify vulnerabilities in Python code and helps beginners understand secure coding concepts and cybersecurity fundamentals.

---

# Features

* Simple Python login application
* Demonstrates insecure coding practices
* Security vulnerability detection using Bandit
* Example of secure coding improvements
* Beginner-friendly cybersecurity project

---

# Technologies Used

* Python
* Visual Studio Code (VS Code)
* Bandit Security Tool

---

# Project Structure

```text id="l6w46q"
SecureCodingReview/
│
├── app.py
├── README.md
```

---

# Vulnerabilities Demonstrated

* Hardcoded Password
* Weak Authentication
* No Password Encryption
* Lack of Input Validation

---

# Installation and Setup

## Step 1: Install Python

Download and install Python from:

```text id="4l86dr"
https://www.python.org/
```

---

## Step 2: Install VS Code

Download Visual Studio Code from:

```text id="gm7x8n"
https://code.visualstudio.com/
```

---

## Step 3: Install Bandit

Open terminal in VS Code and run:

```bash id="e13vki"
pip install bandit
```

---

# Running the Program

Run the Python file using:

```bash id="g74rzs"
python app.py
```

---

# Running Security Analysis

Use Bandit to scan the code:

```bash id="l2wtr0"
bandit app.py
```

---

# Sample Output

## Program Output

```text id="g5gqj6"
Enter Username: admin
Enter Password: 1234
Login Successful
```

---

## Bandit Output

```text id="2ylf7v"
Issue: Hardcoded password string detected
Severity: Medium
Confidence: High
```

---

# Security Improvements

* Use encrypted passwords
* Avoid hardcoded credentials
* Validate user inputs
* Implement secure authentication methods

---

# Result

The project successfully demonstrates how secure coding reviews help identify vulnerabilities and improve application security using static analysis tools.

---

# Author

Developed for cybersecurity and secure coding learning purposes.
