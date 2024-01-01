"""You and your family are at restaurant to have dinner at happyhour offer. You get code coupon code at this offer.
if it matches "happy" word then you will get free deserts. so find out how many free deserts you will get for following code

example coupon_code= "happyishappy"
expected output = 2
"""
coupon_code = input("Enter Coupon Code : ")

print(coupon_code.count("happy"))
