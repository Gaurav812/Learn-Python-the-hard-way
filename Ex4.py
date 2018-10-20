#These first parts indicates what everything is (e.g. there are 100 cars)
cars = 100
#You need the .0 at the end of 4 as it makes the 4 a floating number
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#The bit not in the quotes is still writen but as what is defined above
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be",cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print ("We have", passengers, "to carpool today")
print ("We need to put about", average_passengers_per_car, "in each car.")
