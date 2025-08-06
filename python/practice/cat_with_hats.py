# You have 100 cats. One day you decide to arrange all your cats in a giant circle. 
# Initially, none of your cats have any hats on. 
# You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). 
# Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

# The first round, you stop at every cat, placing a hat on each one.
# The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# The third round, you only stop at every third cat(#3,#6,#9,#12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
# At the end of the 100 rounds, which cats have hats on?

cats_with_hats = []

# We want the laps to be from 1 to 100 instead of 0 to 99
for lap in range(1, 100 + 1):
    for cat in range(1, 100 + 1):

        # Only look at cats that are divisible by the lap
        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)

print(cats_with_hats)