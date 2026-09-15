from pyscript import document, display

def show_order(e):
    document.getElementById("output1").innerHTML = ""
    document.getElementById("output2").innerHTML = ""    
    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)
    pizza = document.getElementById("prod1")
    drinks = document.getElementById("prod2")
    pizza_price = float(pizza.value)
    drink_price = float(drinks.value)
    subtotal = (price + pizza_price + drink_price)
    tax = 0.12 * subtotal
    total = float(tax) + float(subtotal)
    display('===RECEIPT===', target="output1")
    display(f'Subtotal: {subtotal}', target="output2")
    display(f'Tax: {tax}', target="output2", append=True)
    display(f'Total: {total}', target="output2", append=True)
    display(f'Thank you for supporting us! :D', target="output2", append=True)