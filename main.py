from pyscript import display, document

#OPERATIONS
#FLOOR /
# ADD +
# SUBTRACT -
# MODULO %


def create_order(e):
    document.getElementById("output2").innerHTML = "" # clears previous output
    prod1= document.getElementById("item1")
    prod2= document.getElementById("item2")
    prod3= document.getElementById("item3")
    prod4= document.getElementById("item4")
    # Calculate
    subtotal = float(prod1.value) + prod1.checked
    display(subtotal, target="output2")
    subtotal = float(prod1.value) + prod1.checked
    size = document.querySelector('input[name="size"]:checked')
    size_prize = float(size.value)
    grandtotal = subtotal + size_prize
    display(grandtotal, target="output2")