"//span[@class="a-size-medium a-color-base a-text-normal"]/parent::h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]"




"""Positive
1)After clicking on Add to cart the product should be displayed in cart page
2)all the information(image,descriptions,price) should be displayed
3)number of quantity * price should be equal to total cart price
4) after adding to cart proceed to buy should be displayed
5) after dding product into cart user should be able to remove it from cart 
"""

"""Negative
1) empty cart should not display "proceed to buy" or it should display "no items in cart"
2) EMI available dropdown only display when any item is present in cart
3)without clicking on  "This is gift", checkbox gift should not be offered
4)item in cart is suppose out of stock it should not be proceed to buy product
5)  
"""
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


Person = person("kunal",30)

driver.switch_to.alert.dismiss()

