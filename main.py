from pyscript import document, display

def show_order(e):
    document.getElementById("output1").innerHTML = ""
    document.getElementById("output2").innerHTML = ""    
    size = document.querySelector("input[name='size']:checked") #selects input fields with the keyword 'size'
    price = float(size.value) #retrieves the value from the radio input
    pizza = document.getElementById("prod1") 
    drinks = document.getElementById("prod2")
    pizza_price = float(pizza.value) 
    drink_price = float(drinks.value)
    subtotal = (price + pizza_price + drink_price) #adds the prices from the input and select fields to generate an initial price (without tax)
    tax = 0.12 * subtotal #calculates the tax prices from overall items
    grandtotal = float(tax) + float(subtotal) #calculates the final price of overall items including tax
    display('===RECEIPT===', target="output1")
    display(f'Subtotal: {subtotal}', target="output2")
    display(f'Tax: {tax // 1}', target="output2", append=True)
    display(f'Total: {grandtotal // 1}', target="output2", append=True)
    display(f'Thank you for supporting us! :D', target="output2", append=True)
