import copy


# Function 1
def create_inventory():

    inventory = [

        {
        "item":"Laptop",
        "details":{
            "price":50000,
            "stock":10,
            "supplier_rating":4.8
        }
        },

        {
        "item":"Phone",
        "details":{
            "price":20000,
            "stock":25,
            "supplier_rating":4.5
        }
        },

        {
        "item":"Tablet",
        "details":{
            "price":30000,
            "stock":15,
            "supplier_rating":4.6
        }
        }

    ]

    return inventory



# Function 2
def apply_discount(data,index):

    data[index]["details"]["price"] *= 0.9

    data[index]["details"]["stock"] += 5

    data[index]["details"]["supplier_rating"] = 5.0



# Function 3
def compare_data(original,modified):

    changed=0
    unchanged=0

    for i in range(len(original)):

        if original[i]!=modified[i]:
            changed+=1
        else:
            unchanged+=1

    return (changed,unchanged)



# MAIN

inventory=create_inventory()

# Copies
shallow_copy=copy.copy(inventory)

deep_copy=copy.deepcopy(inventory)


# Personal mutation rule
index_to_modify=2 % len(inventory)


# Mutate copies
apply_discount(
shallow_copy,
index_to_modify
)

apply_discount(
deep_copy,
index_to_modify
)


summary=compare_data(
inventory,
deep_copy
)


print("\nOriginal Inventory")
for item in inventory:
    print(item)


print("\nShallow Copy")
for item in shallow_copy:
    print(item)


print("\nDeep Copy")
for item in deep_copy:
    print(item)


print("\nDifferences Observed:")
if inventory[index_to_modify]==shallow_copy[index_to_modify]:
    print(
    "Shallow copy mutation affected original data"
    )

if inventory[index_to_modify]!=deep_copy[index_to_modify]:
    print(
    "Deep copy remained independent"
    )


print("\nTuple Summary:")
print(summary)