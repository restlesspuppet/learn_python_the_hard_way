name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm = height * 2.54
kg = weight * 0.454

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall (or about {round(cm)} centemeters).")
print(f"He's {weight} pounds heavy (or about {round(kg)} kilograms).")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")
