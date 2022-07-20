import greeter
# Default is "World"
# Author: Jim Weirich (jim@somewhere.com)
arg = input() or "World"

greeter = Greeter.new(arg)
print(greeter.greet)