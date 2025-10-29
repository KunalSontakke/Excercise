input= "PrOgRaMM"
# #
# # Expected output
# Result is: pRoGrAmm
print("".join([i.lower() if i.isupper() else i.upper() for i in input]))
