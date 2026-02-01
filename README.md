# List Manipulator (Python)

## Project Description

List Manipulator is a console-based Python program developed as part of the Python Fundamentals course at SoftUni.
The task simulates a real-world programming assignment where a developer must manipulate a list of integers using a predefined set of commands.

The program reads an initial list of integers and then processes commands that modify the list or extract information from it.
The goal is to correctly interpret each command, handle edge cases, and produce the expected output exactly as specified.

## Project Goal

The main objective of this project is to:

- Practice list manipulation in Python
- Apply conditional logic
- Handle edge cases and validation
- Follow strict input and output requirements

## Supported Commands

### exchange {index}

Splits the list after the given index and exchanges the two resulting sub-lists.

Example:
[1, 2, 3, 4, 5] -> exchange 2 -> [4, 5, 1, 2, 3]

Rules:
- If the index is outside the list boundaries or negative, print "Invalid index"

### max even / odd

Prints the index of the maximum even or odd element in the list.

Rules:
- If multiple elements have the same maximum value, return the rightmost index
- If no matching element exists, print "No matches"

### min even / odd

Prints the index of the minimum even or odd element in the list.

Rules:
- If multiple elements have the same minimum value, return the rightmost index
- If no matching element exists, print "No matches"

### first {count} even / odd

Returns the first count even or odd elements from the list.

Rules:
- If count is greater than the list length, print "Invalid count"
- If fewer elements are available, return as many as possible
- If no matching elements exist, print an empty list []

### last {count} even / odd

Returns the last count even or odd elements from the list.

Rules:
- If count is greater than the list length, print "Invalid count"
- If fewer elements are available, return as many as possible
- If no matching elements exist, print an empty list []

### end

Stops processing commands and prints the final state of the list.

## Input Format

- The first line contains a list of integers separated by a single space
- Each of the following lines contains a command
- The command "end" terminates the input

The input is always valid and follows the described format.

## Output Format

- Each command that produces output prints its result on a separate line
- After the "end" command, the final list is printed in square brackets
- Elements in the final list are separated by a comma and a space

## Constraints

- Number of commands: from 2 to 50
- Number of list elements: from 1 to 50
- List elements are integers in the range from 0 to 1000
- Index values are integers in the range [-2^31 to 2^31 - 1]
- Count values are integers in the range [1 to 2^31 - 1]
- Time limit: 0.1 seconds
- Memory limit: 16 MB

## Learning Outcomes

This project helps develop skills in:

- Python list operations and slicing
- Filtering data based on conditions
- Managing program state across multiple commands
- Writing clean and readable Python code
- Implementing precise input and output handling

