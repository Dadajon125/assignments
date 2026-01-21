
prices = {"bath": 15.00,
    "trim": 25.00,
    "full": 40.00
    }


total = 0.0

print("welcome to the Pet Grooming Salon Pricing Calculator!")
print("available services:")
for service, price in prices.items():
    print(f" - {service.capitalize()}: ${price:.2f}")
print("Type 'done' when finished.\n")

while True:
    service = input("Enter a service (bath/trim/full) or 'done' to finish: ")

    if service == "done":
        break
    elif service in prices:
        total += prices[service]
        print(f"added {service} (${prices[service]:.2f}). Current total: ${total:.2f}")
    else:
        print( " Please enter 'bath', 'trim', 'full', or 'done'.")

discount = 0
if total >= 75:
    discount = 12
    total = discount


print(" ------- RECEIPT -------")
print(f"Subtotal: ${total + discount:.2f}")
if discount > 0:
    print(f"multi-pet discount applied: -${discount:.2f}")
print(f"final Total: ${total:.2f}")
print("----------------------")
print("Thank you for choosing our salon! ")