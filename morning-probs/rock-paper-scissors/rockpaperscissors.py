num_matches = int(input())
alice_round_score = 0
bob_round_score = 0
for i in range(num_matches):
    # now you do the rest!
    # read in the rounds in this match
    # example: if the line of input was "RR RP SR" then
    # rounds == ["RR", "RP", "SR"]
    alice_score = 0
    bob_score = 0
    user_input = input()
    user_input_list = []
    user_input_list.extend(user_input.split())
    for k in range(0, len(user_input_list)):
        if user_input_list[k] == "RS" or user_input_list[k] == "SP" or user_input_list[k] == "PR":
            alice_score += 1
        elif user_input_list[k] == "SR" or user_input_list[k] == "PS" or user_input_list[k] == "RP":
            bob_score += 1
        elif user_input_list[k] == "RR" or user_input_list[k] == "PP" or user_input_list[k] == "SS":
            alice_score += 0
            bob_score += 0

    if alice_score > bob_score:
        alice_round_score += 1
    elif bob_score > alice_score:
        bob_round_score += 1
    else:
        alice_round_score += 0
        bob_round_score += 0

# print here whoever is the overall winner of all the matches and
# how many matches the winner won
if alice_round_score > bob_round_score:
    print("Alice", alice_round_score)
elif alice_round_score == bob_round_score:
    print("Alice", alice_round_score)
else:
    print("Bob", bob_round_score)
