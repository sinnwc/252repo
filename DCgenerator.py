print("How many turns are in the generator coil?")
n = float(input())
print("What is the length of one side of the coil in meters?")
l = float(input())
print("What is the field strength in Teslas?")
B = float(input())
print("What is the rate that the coil turns per second?")
w = float(input())

op = n*(l*l)*B*w

print(f"The generator will produce {round(op, 2)} volts.")