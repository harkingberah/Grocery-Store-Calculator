print("Welcome to Samson's Grocery Store.")

def find_price(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return -1

items = {
    "sugar": 200,
    "salt": 150,
    "bread": 400,
    "soap": 600,
    "eggs": 350,
    "milk": 1050,
    "biscuit": 700
    }

# Display the available items to the user
print("Here are the items we have in store:")
for item, price in items.items():
    print(f"{item}\t\t{price}")

# Initialize variables
scanned_items = []
total_due = 0
# Start scanning items
while True:
    item = input("Enter an item to scan (or 'done' to finish): ").lower()

    if item == "done":
        break

    price = find_price(items, item)

    if price == -1:
        print("Item not found. Please scan a valid item.")
    else:
        quantity = int(input("Enter the quantity: "))
        scanned_items.append((item, price, quantity))
        sub_total=price * quantity
        total_due = total_due+sub_total

# Display the receipt
print("\nReceipt:")
print("Item\t\tPrice\t\tQuantity\tSub-total")

for item, price, quantity in scanned_items:
    sub_total = price * quantity
    print(f"{item}\t{price}\t\t{quantity}\t\t{sub_total}")


print(f"Total Amount Due: {total_due}")