# encoding:utf-8

def input_positive_integer(prompt):

  while True:
    input_value = int(input(prompt))
    if input_value > 0:
      return input_value

mass = input_positive_integer("Enter the mass(positive_integer): ")

acceleration = input_positive_integer("Enter the acceleration(positive_integer): ")
print("The Force is", mass * acceleration)