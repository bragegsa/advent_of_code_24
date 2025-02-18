# Advent of Code 2024 -Solutions in Python and C++
This is a solution of advent of code 2024. The tasks can be found here: 

- [Advent of Code](https://adventofcode.com/)

## How to run:

The all_solutions.py script presents all solutions for the different daily tasks up to (and including) day 5.

To present the solutions for the other daily tasks, run the C++ project.

### Packages needed for python project
The python project uses the following packages:

- ![NumPy](https://img.shields.io/badge/NumPy-2.2.0%2B-blue)
- ![Pandas](https://img.shields.io/badge/Pandas-2.2.3%2B-green)
- ![PyTest](https://img.shields.io/badge/PyTest-8.3.4%2B-green)
- ![re](https://img.shields.io/badge/re-module-blue)


### How to build C++ project

To build the C++ project, you need to do the following:

```bash
# Build the project
make

# Run the project
./main

```

If you want to remove the generated executable, run the following:

```bash
# Remove generated executable
make clean

```

### How to run python tests

In the terminal, from the repository origin, run the following command:

```bash
# Run python test scripts
pytest

```

It is also possible to use the VSCodes Testing interface to run spesific functions.

## Structure

The project is split into two parts. The first 5 daily tasks are done in python and the other days are done in C++.

### modules
This folder includes a module for each of the daily puzzles. Each module can be run directly if needed. The sub-folder /tests includes test scripts that insures the python modules run correctly and as expected. 

### modules_cpp

This folder includes a module for each of the daily puzzles from day 6 and onwards. To run these modules, run the C++ project.

### inputs

This folder includes the input data for the different daily tasks.
