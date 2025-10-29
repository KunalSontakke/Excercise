# dic1 = {"name":"kunal","age":31,"company":"nitor","location":"nagpur"}
# print(dic1["location"])

# dict.items()get("key","dafault")

with open("Int_cyient_L2_a","r") as file:
    content1 = file.read()
    print(content1)

    with open("Int_Cyient_L2_b","w") as file_b:
        file_b.write(content1)

