
  <div align="center">
  <h1 align="center">Sum of Digits</h1>
  <h3>Codebase for the Sum of Digits</h3>
  <h3>◦ Developed with the software and tools below.</h3>
  <p align="center"><img src="https://img.shields.io/badge/-Python-004E89?logo=Python&style=flat-square" alt='Python\' />
  </p>
  </div>
  
  ---
  ## 📚 Table of Contents
  - [📚 Table of Contents](#-table-of-contents)
  - [🔍 Overview](#-overview)
  - [🌟 Features](#-features)
  - [📁 Repository Structure](#-repository-structure)
  - [💻 Code Summary](#-code-summary)
  - [🚀 Getting Started](#-getting-started)
  
  ---
  
  
  ## 🔍 Overview

 The project contains a Python script named sum_of_digits.py and a unit test file named unit_test.py

---

## 🌟 Features

 sum_of_digits.py, unit_test.py

---

## 📁 Repository Structure

```sh
├── sum_of_digits.py
└── unit_test.py

```

---

## 💻 Code Summary

<details><summary>Root</summary>

| File | Summary |
| ---- | ------- |
| sum_of_digits.py |  The code defines a function called `sum_of_digits` that takes an integer `n` as input and calculates the sum of its digits using a recursive function called `calculate_sum_of_digits`. The `sum_of_digits` function prompts the user to input an integer, calls `calculate_sum_of_digits` with the input `n`, and prints the result. The `calculate_sum_of_digits` function recursively calculates the sum of the digits of `n` by taking the absolute value of `n`, returning 0 if `n` is 0, and otherwise returning the last digit of `n` plus the result of calling `calculate_sum_of_digits` with the remaining digits. The overall time complexity of the program is O(log n), where n is the input integer. |
| unit_test.py |  The code defines a function to calculate the sum of the digits of a positive integer, and also includes test cases for the function using the unittest module in Python. |

</details>

---

## 🚀 Getting Started

 To get started with this project, follow these steps:<br>
1. Open a terminal or command prompt and navigate to the directory where you cloned the repository.
2. Run the unit tests to ensure that everything is working as expected: `python -m unittest discover`
3. Once the unit tests pass, you can run the script by typing: `python sum_of_digits.py`
4. The script will prompt you to enter a list of numbers, separated by spaces. Enter the numbers and press enter.
5. The script will then calculate the sum of the digits in the list and print the result.

That's it! You should now be able to use the script to calculate the sum of digits in a list of numbers.

---

Generated with ❤️ by [ReadMeAI](https://www.readmeai.co/).
