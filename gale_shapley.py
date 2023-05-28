n = int(input("Input the number of people in each set: "))
A_offers = input("Does group A or B make the offers? ") == "A"
matches = [0] * (n + 1)  # a_i is matched to b_{matches[i]}


def print_matches():
    print("Matches: ", end="")
    for i in range(1, n + 1):
        if matches[i] != 0:
            print("(a_" + str(i) + ", b_" + str(matches[i]) + ")", end=" ")
    print("\n")


def accept_matching(curr, target):
    if A_offers:
        matches[curr] = target
    else:
        matches[target] = curr
    print("Accepted")
    print_matches()


# Collect preference lists
preference_A, preference_B = [[]], [[]]
for i in range(1, n + 1):
    preferences = input("a_" + str(i) + "'s preferences: ").split()
    preference_A.append(list(map(int, preferences)))
for i in range(1, n + 1):
    preferences = input("b_" + str(i) + "'s preferences: ").split()
    preference_B.append(list(map(int, preferences)))
print()

unmatched = [i for i in range(1, n + 1)]
while unmatched:
    curr = unmatched.pop(0)
    curr_preferences = preference_A[curr] if A_offers else preference_B[curr]

    while curr_preferences:
        target = curr_preferences.pop(0)
        if A_offers:
            print("a_" + str(curr) + " propositions " + "b_" + str(target), end=": ")
        else:
            print("b_" + str(curr) + " propositions " + "a_" + str(target), end=": ")
        if A_offers and target in matches or not A_offers and matches[target] != 0:
            # Target already has a partner
            existing_partner = matches.index(target) if A_offers else matches[target]
            target_preferences = (
                preference_B[target] if A_offers else preference_A[target]
            )
            if target_preferences.index(curr) < target_preferences.index(
                existing_partner
            ):
                # Target rejects existing partner
                unmatched.append(existing_partner)
                if A_offers:
                    matches[existing_partner] = 0
                accept_matching(curr, target)
                break
            else:
                print("Rejected")
                print_matches()
        else:  # Target is unmatched
            accept_matching(curr, target)
            break
