from pyscript import document, display

def create_order(e):
    document.getElementById("Subtotal").innerHTML = "" # clears previous output, applies to VAT TAX and Total Amount
    document.getElementById("VAT").innerHTML = ""
    document.getElementById("Total Amount").innerHTML = ""

    curry = document.getElementById('Curry') 
    curryprice = float(curry.value) * curry.checked

    coffee = document.getElementById('Coffee')
    coffeepice = float(coffee.value) * coffee.checked

    Udon = document.getElementById('Udon')
    Udonprice = float(Udon.value) * Udon.checked

    futabacake = document.getElementById('Futaba Cake')
    futabacakeprice = float(futabacake.value) * futabacake.checked

    callingcard = document.getElementById('Calling Card')
    callingcardprice = float(callingcard.value) * callingcard.checked

    sub = curryprice + coffeepice + Udonprice + futabacakeprice + callingcardprice

    vat = sub * 0.12 

    total = vat + sub 


    Sub = f"Subtotal: ₱{sub:.2f}"
    display(Sub, target = "Subtotal") 

    Vat = f"VAT: ₱{vat:.2f}"
    display(Vat, target = "VAT")

    Total = f"Total: ₱{total:.2f}"
    display(Total, target = "Total Amount")