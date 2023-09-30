# RLBasics

This application is used to simulate an Agent-Environment Interaction.

## Code Structure:

- State.py : Contains State Definition including policy, transition and rewards
- Environment.py : Defines objects of State (all 7 states)
- Episode.py : Runs one Episode taking as input set of states and gamma.
- Functions.py : Contains all helper functions
- RunConstantPolicy.py : Main function to be run for questions 2a, 2b and 2c.
- RunRandomPolicy.py : Main function to be run for question 2d.

## Setup:

- Requires python3 to be installed. 
- Python version used to test is Python 3.11.5
- Requires numpy and matplotlib packages.
- Command: python RunConstantPolicy.py
- Command: python RunRandomPolicy.py
