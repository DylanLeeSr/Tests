#Coding a For loop that represents something in work or personal life.

#I am creating a shopping list that verifies items in your cart.

shoppingList = ["milk","eggs", "LaCroix", "Coffee"]

shoppingCart = ["milk", "eggs", "LaCroix"]

#for loop showing items that are on the list and in the cart by displaying "in cart"
for items in shoppingList and shoppingCart:
    print(f"{items} in cart")

#list comprehension comparing items in the two lists and displaying what is not in the cart with a reminder "Dont forget the"
dontForget = [items for items in shoppingList if items not in shoppingCart]

print(f"Dont forget the {dontForget}!")