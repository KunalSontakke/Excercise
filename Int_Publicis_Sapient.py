str1 = "kunal"

if str1 == str1[::-1]:
    print(f"{str1} is palindrome")

else:
    print(f"{str1} is not palindrome")

# ===================================================================================
"""POST https://api.bookstore.com/orders
Description: This API creates a new book order.
Request Body Example:
 
 
{
    "customerId": 12345,
    "bookId": "BK-789",
    "quantity": 2,
    "paymentMethod": "CreditCard"
}
"""