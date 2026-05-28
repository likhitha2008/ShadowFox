import random

count_6 = 0
count_1 = 0
double_6 = 0
previous_roll = 0

for i in range(20):
    roll = random.randint(1, 6)
    print("Roll:", roll)

    if roll == 6:
        count_6 += 1

    if roll == 1:
        count_1 += 1

    if previous_roll == 6 and roll == 6:
        double_6 += 1

    previous_roll = roll

print("Number of times 6 appeared:", count_6)
print("Number of times 1 appeared:", count_1)
print("Number of times two 6 appeared in a row:", double_6)