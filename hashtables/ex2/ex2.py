#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    ticket_table = {}
    source = ''
    # create a hashtable with key/value pairs. The source is the key and the value is the destination 
    for i in tickets:
        ticket_table[i.source] = i.destination
    
    # first route is the ticket with source of none
    route.append(ticket_table['NONE'])
    # set the variable i to equal the value of the first key/destination
    i = ticket_table['NONE']
    # loop through the hashtable of all the destinations
    for t in ticket_table:
        # check if the next destination is in the table and is not the first destination
        if i in ticket_table and i is not 'NONE':
            # set the source to be the value of this destination
            source = ticket_table[i]
            # append that source to the route
            route.append(source)
            # set the variable i to the next destination and repeat process
            i = source        
        
    return route
    #NONE --> destination
    #detination --> source
    #source --> destination
    #destination --> source
    #source --> NONE


# tickets = [
#     Ticket( source: "PIT", destination: "ORD" ),
#     Ticket( source: "XNA", destination: "CID" ),
#     Ticket( source: "SFO", destination: "BHM" ),
#     Ticket( source: "FLG", destination: "XNA" ),
#     Ticket( source: "NONE", destination: "LAX"),
#     Ticket( source: "LAX", destination: "SFO" ),
#     Ticket( source: "CID", destination: "SLC" ),
#     Ticket( source: "ORD", destination: "NONE"),
#     Ticket( source: "SLC", destination: "PIT" ),
#     Ticket( source: "BHM", destination: "FLG" )
# ]


ticket1 = Ticket("PIT", "ORD" )
ticket2 = Ticket("XNA", "CID" )
ticket3 = Ticket("SFO", "BHM" )
ticket4 = Ticket("FLG", "XNA" )
ticket5 = Ticket("NONE", "LAX")
ticket6 = Ticket("LAX", "SFO" )
ticket7 = Ticket("CID", "SLC" )
ticket8 = Ticket("ORD", "NONE")
ticket9 = Ticket( "SLC", "PIT" )
ticket10 = Ticket("BHM", "FLG" )

tickets = [
ticket1,
ticket2,
ticket3,
ticket4,
ticket5,
ticket6,
ticket7,
ticket8,
ticket9,
ticket10,
]

print(reconstruct_trip(tickets, 2))


# input 
    # list of Ticket classes 
        # source string represents the starting airport 
        # destination string represents the next airport along the trip 
    # ticket for first flight has a destination with a `source` of`NONE`
    # ticket for your final flight has a `source` with a `destination` of `NONE`. 

# ouput 
    #Your function should output an array of strings with the entire route of
    #your trip. For the above example, it should look like this:
    #["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]