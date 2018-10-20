#Ex6

#variable
types_of_people = 10
#simply strat of joke
x = f"There are {types_of_people} types of people."

#another two variables
binary = "binary"
do_not = "don't"
#answer to question
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

#joke_evaluation is a variable
#when it says hilarious is false the format completes the
#sentence. Instead of writing f we put 'format.' It formats
#hilarious as false. You only put f when it encorporates quotation

print (joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
