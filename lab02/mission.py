#Jonathan Wales CIS109 LAB 2: Mission Briefing

#Part 1-Mission Information
name = input("Enter your agent name: ")
age = input("Enter your age: ")
training_years = input("Enter the number of years you have been training: ")
favorite_color = input("Enter your favorite color: ")
gadgets = input("Enter the number of gadgets you are carrying: ")
minutes = input("Enter the number of minutes you have to complete the mission: ")

#Part 2-Calculate Mission Statistics  
# Create variables and expressions that calculate the following.

#1. Training Percentage

if int(age) > 0:
    training_percentage = (int(training_years) / int(age)) * 100
else:
    training_percentage = 0.0

#Store the result in:  training_percentage

#2. Gadget Density

if int(training_years) > 0:
    gadget_density = int(gadgets) / int(training_years)
else:
    gadget_density = 0.0

#Store the result in:  gadget_density

#3. Mission Seconds

mission_seconds = int(minutes) * 60


#Store the result in:  mission_seconds

#4. Mission Countdown

mission_time_remaining = int(minutes) - 7


#Store the result in:  mission_time_remaining

#Part 3 — Create a Mission Code
#Create a variable called:

mission_code = name.upper() + "-" + favorite_color.upper() + "-" + age

"""The mission code should be created by combining:

The agent's name
Their favorite color
Their age
For example:

Agent: Morgan
Color: blue
Age: 24
could produce:  MORGAN-BLUE-24
Hint: You can use string methods such as .upper().

Part 4 — Boolean Expressions
Create Boolean expressions that answer these questions:"""

is_adult = int(age) >= 18
has_many_gadgets = int(gadgets) >= 5
has_training_experience = int(training_years) > 0

"""Use the following rules:

is_adult is True if the agent is at least 18.
has_many_gadgets is True if the agent has at least 5 gadgets.
has_training_experience is True if the agent has trained for more than 0 years.

Part 5 — Mission Briefing
Use print() statements to produce a final mission briefing."""
print("====================================")
print("        SECRET MISSION BRIEFING")
print("====================================")
print()
print(f"Agent: {name}")
print(f"Mission Code: {mission_code}")
print()
print(f"Age: {age}")
print(f"Training: {training_years} years")
print(f"Training Percentage: {training_percentage:.2f}%")
print()
print(f"Gadgets: {gadgets}")
print(f"Gadget Density: {gadget_density:.2f} per training year")
print()
print(f"Mission Time: {minutes} minutes")
print(f"Mission Time Remaining: {mission_time_remaining} minutes")
print(f"Mission Time in Seconds: {mission_seconds}")
print()
print(f"Adult Agent: {is_adult}")
print(f"Many Gadgets: {has_many_gadgets}")
print(f"Training Experience: {has_training_experience}")
print()
print("====================================")
print("        GOOD LUCK, AGENT!")
print("====================================")
"""Your output should contain all of the following:

====================================
        SECRET MISSION BRIEFING
====================================
 
Agent: Morgan
Mission Code: MORGAN-BLUE-24
 
Age: 24
Training: 5 years
Training Percentage: 20.83%
 
Gadgets: 4
Gadget Density: 0.80 per training year
 
Mission Time: 37 minutes
Mission Time Remaining: 30 minutes
Mission Time in Seconds: 2220
 
Adult Agent: True
Many Gadgets: False
Training Experience: True
 
====================================
        GOOD LUCK, AGENT!
===================================="""