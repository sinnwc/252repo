total_sum = 0 #declare sum total
for i in range(1000): #creating the range
    if i % 3 == 0 or i % 5 == 0: #using mods to figure out multiples of 3 or 5
        total_sum = total_sum + i #adding final sum to current i value
print(total_sum) # printing the return