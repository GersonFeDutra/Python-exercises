list1 = ["coperaite", 123, "loren", "ipsun", "dolor", "/33m1fBlue", "findme"]
list2 = [532, "lor", "iplon", list1, "/33mF3Red", "findme", "brr", 42]

def comparison():

    for value_i in list1:

        for value_j in list2:

            if value_i == value_j:
                return value_i

print(comparison())
