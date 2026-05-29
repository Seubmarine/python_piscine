import sys

if len(sys.argv) < 2:
    print()
    exit(0)
if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided\n")
    exit(0)

try:
    int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer\n")
    exit(0)

if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.\n")
else:
    print("I'm Odd.\n")
