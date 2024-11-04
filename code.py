contacts={"adil muhammed":{
    "contact":9995089700,"email":"adil123@gmail.com","address":"al amana"},
    "mushraf":{"contact":1234567890,"email":"mushraf456@gmail.com","address":"ilahi manzil"
           },"nizar":{"contact":8775555555,"email":"nizar858@gmail.com","address":"naseemas"}}

while True:
    try:
        z = input("enter the contact name to access")
        if z in contacts:
            print(contacts[z])
            break
        else:
            print("provided wrong information")

    except KeyError:
           print("provided wrong input")
