#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(0, len(weights)):
    # store each weight in the input list as keys (weights[i])
    # store each weight's list index as its value (i)
        value = hash_table_retrieve(ht, limit - weights[i])
        # check to see if the hash table contains an entry for `limit - weight`
        if value is not None:
            # If it does, then we've found the two items whose weights 
            # sum up to the `limit`!
            return (i, value)
        else:
            hash_table_insert(ht, weights[i], i)

    return None




def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + "" + answer[1]))
    else:
        print("None")


weights_1 = [9]
answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
print(f"Should be None: {answer_1}")

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(f"Should be (1, 0): {answer_2}")

weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(f"Should be (3, 1): {answer_3}")

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(f"Should be (6, 2): {answer_4}")