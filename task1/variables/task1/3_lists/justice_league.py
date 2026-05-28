justice_league = ["Batman", "Superman", "Wonder Woman",
                  "Flash", "Aquaman", "Green Lantern"]

# 1. Number of members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("After adding members:")
print(justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("After making Wonder Woman leader:")
print(justice_league)

# 4. Separate Aquaman and Flash by moving Green Lantern
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index + 1, "Green Lantern")

print("After separating Aquaman and Flash:")
print(justice_league)

# 5. Replace team with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl",
                  "Martian Manhunter", "Green Arrow"]

print("New Justice League:")
print(justice_league)

# 6. Sort alphabetically and find new leader
justice_league.sort()

print("Sorted Justice League:")
print(justice_league)

print("New leader:", justice_league[0])