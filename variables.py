# 1. Declare and initiate all the variables for this project
        # Use the given variable names and values to do so, if the variable has no value, then you need to do some math to calculate it's vale, E.G. average_passengers_per_bus = passengers / buses_driven
  
buses = 100
space_in_a_bus = 200.0
drivers = 30
passengers = 130
buses_not_driven = (buses-drivers)
buses_driven = drivers
total_capacity = (drivers*space_in_a_bus)
average_passengers_per_bus = (passengers/buses_driven)


# 2. Print the obtained values in useful sentences, E.G. print "There are", buses, "buses available."

print("there are", buses, "buses available.")
print("there are only", drivers, "drivers available.")
print("there will be", buses_not_driven, "empty buses today.")
print("we can transport", total_capacity, "people today.")
print("we have", passengers, "to buspool today.")
print("we need to put about", average_passengers_per_bus, "in each bus")