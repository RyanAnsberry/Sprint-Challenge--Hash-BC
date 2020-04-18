#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    answer = []
    # store each weight in the input list as keys
    keys = weights
    # store each weight's list index as its value
    for i in range(len(keys)):
        hash_table_insert(ht, keys[i], i)
    # check to see if the hash table contains an entry for `limit - weight`
    for i in range(len(keys)):
        if hash_table_retrieve(ht, limit - keys[i]):
        # If it does, then we've found the two items whose weights sum up to the `limit`!
            answer.append(i)
        else:
            return None
    print_answer(answer)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + "" + answer[1]))
    else:
        print("None")

weights = [ 4, 6, 10, 15, 16 ]
get_indices_of_item_weights(weights, 5, 21)
# Should be "3 1"