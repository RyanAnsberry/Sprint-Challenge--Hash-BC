#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    # -1 length to account for unwanted nones in route
    route = [None] * (length-1)

    # insert all tickets into hashtable. insert( key=source, value=destination)
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
    
    # start route at ticket sourced as 'NONE', the destination will be the 1st route location
    route[0] = hash_table_retrieve(hashtable, "NONE")
    # iterate trough the tickets starting from the 2nd element
    for i in range(1, length-1):
        # assign value of next destination to the hashtable value of the last route destination
        next_destination = hash_table_retrieve(hashtable, route[i-1])
        # check if val is not none
        if next_destination:
            # add the next destination to the route
            route[i] = next_destination

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
result = reconstruct_trip(tickets, 3)
print(f"Expected: ['PDX', 'DCA'] | Result: {result}")



ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
result = reconstruct_trip(tickets, 10)
print(f"Expected: ['LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'SAP', 'SLC', 'PIT', 'ORD'] | Result: {result}")
