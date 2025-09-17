class product:
    def __init__(self,name,code,categeoy,price):
        self.name = name
        self.code = int(code)
        self.categeoy = categeoy
        self.price = int(price)
class Category:
    def __init__(self,name,code,no_of_product=0):
        self.name=name
        self.code = code
        self.no_of_product = int(no_of_product)



cat1=Category("Smart Home Devices","0001")
cat2=Category("Home Appliances","0002")
cat3=Category("Audio & Speakers","0003")
co=[cat1,cat2,cat3]
po=[
product("Echo Dot (5th Gen)","001",cat1,"6000"),
product("Dyson V15 Detect","002",cat2,"1000"),
product("Google Nest Thermostat","003",cat1,"2000"),
product("JBL Flip 6","004",cat3,"8000"),
product("Instant Pot Duo 7-in-1","005",cat2,"5000"),
product("Philips Hue Smart Bulb","006",cat1,"1500"),
product("Sony WH-1000XM5","007",cat3,"6000"),
product("LG Front Load Washing Machine","008",cat2,"8000"),
product("Ring Video Doorbell 4","009",cat1,"6000"),
product("Bose SoundLink Revolve+ II","010",cat3,"4000")
]
for cat in co:
    for prod in po:
        if cat.code == prod.categeoy.code:
            cat.no_of_product += 1

for c in co:
    print(c.name,c.code, c.no_of_product)
for i in range(len(po)):
    for j in range(i+1,len(po)):
        if po[j].price < po[i].price:
            po[j],po[i]=po[i],po[j]

print("low to high---------------------------")
for i in po:
    print(i.name,i.code,i.price)

print("high to low------------------------------------")
for i in range(len(po)):
    for j in range(i+1,len(po)):
        if po[j].price > po[i].price:
            po[j],po[i]=po[i],po[j]

for i in po:
    print(i.name,i.code,i.price)
srch=int(input("search the product:"))

for i in range(len(po)):
    if srch == po[i].code:
        print(po[i].name,po[i].code,po[i].price)
        break
    else:
        i+=1
else:
    print("not found")
