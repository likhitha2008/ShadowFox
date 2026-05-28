total_jumping_jacks = 0

for i in range(1, 11):

    print("Perform 10 jumping jacks")
    total_jumping_jacks += 10

    answer = input("Are you tired? (yes/no): ")

    if answer == "yes":
        skip = input("Do you want to skip the remaining sets? (yes/no): ")

        if skip == "yes":
            print("You completed a total of", total_jumping_jacks, "jumping jacks")
            break

    remaining = 100 - total_jumping_jacks

    if remaining > 0:
        print(remaining, "jumping jacks remaining")

else:
    print("Congratulations! You completed the workout")