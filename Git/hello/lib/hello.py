from greeter import Greeter

# Default is World
# Author: Karolina (email@gmail.com)

print("What's your name?")

name = input("name = ")

print("Hello ", name, "!")

greeter = Greeter(name)

print(greeter.greet())