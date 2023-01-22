# you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples where the first element is the
# index and the second is the value. [(index, value)]. accordingly, elements with an even index are
# placed in another list of tuples with the same format as in the case with odd indices

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
odds = []
evens = []

# for number in my_list:
#     if number % 2 == 0:
#         evens.append(number)
#     else:
#         odds.append(number)
# odds = list(enumerate(odds))
# evens = list(enumerate(evens))
# print(odds)
# print(evens)

for num in range(0, len(my_list)):
    if num % 2 == 0:
        evens.append((num, my_list[num]))
    else:
        odds.append((num, my_list[num]))
print(odds)
print(evens)


# You have 2 lists of names friends = ["John", "Marta", "James"] and enemies = ["John", "Johnatan", "Artur"].
# Loop through the names of friends and write the message f"{friend} we are the best friends"
# if the friend is not in the list of enemy names. And display the message f"{friend} we are not
# friends anymore" if the friend is on the list of enemies. If the friend's name is James, we don't
# check him because he is the best friend.

friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for friend in friends:
    if friend == "James":
        continue
    elif friend in enemies:
        print(f"{friend}, we are not friends anymore")
    else:
        print(f"{friend},  we are the best friends")
