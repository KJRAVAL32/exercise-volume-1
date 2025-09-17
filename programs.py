class Product:
    def __init__(self, name, code, categeoy, price):
        self.name = name
        self.code = int(code)
        self.categeoy = categeoy
        self.price = int(price)


class Category:

    def __init__(self, name, code, no_of_product=0):
        self.name = name
        self.code = code
        self.no_of_product = int(no_of_product)

    @staticmethod
    def sort_l_to_h():

        for i in range(len(po)):
            for j in range(i + 1, len(po)):
                if po[j].price < po[i].price:
                    po[j], po[i] = po[i], po[j]
        print("low to high---------------------------")
        for i in po:
            print(f"Name: {i.name}, Code: {i.code}, Price: {i.price}")

    @staticmethod
    def sort_h_to_l():
        print("high to low------------------------------------")
        for i in range(len(po)):
            for j in range(i + 1, len(po)):
                if po[j].price > po[i].price:
                    po[j], po[i] = po[i], po[j]

        for i in po:
            print(f"Name: {i.name}, Code: {i.code}, Price: {i.price}")

    def search(self,po):
        srch = int(input("search the product:"))
        for i in range(len(po)):
            if srch == po[i].code:
                print(po[i].name, po[i].code, po[i].price)
                break
            else:
                i += 1
        else:
            print("not found")

    def print_cate(self, co, po):
        for cat in co:
            cat.no_of_product = 0
            for prod in po:
                if cat.code == prod.categeoy.code:
                    cat.no_of_product += 1
        for c in co:
            print(f"Name: {c.name}, Code: {c.code}, No of products: {c.no_of_product}")

cat1 = Category("Smart Home Devices", "1")
cat2 = Category("Home Appliances", "2")
cat3 = Category("Audio & Speakers", "3")
co = [cat1, cat2, cat3]
po = [
    Product("Echo Dot (5th Gen)", "001", cat1, "6000"),
    Product("Dyson V15 Detect", "002", cat2, "1000"),
    Product("Google Nest Thermostat", "003", cat1, "2000"),
    Product("JBL Flip 6", "004", cat3, "8000"),
    Product("Instant Pot Duo 7-in-1", "005", cat2, "5000"),
    Product("Philips Hue Smart Bulb", "006", cat1, "1500"),
    Product("Sony WH-1000XM5", "007", cat3, "6000"),
    Product("LG Front Load Washing Machine", "008", cat2, "8000"),
    Product("Ring Video Doorbell 4", "009", cat1, "6000"),
    Product("Bose SoundLink Revolve+ II", "010", cat3, "4000")
]

cat1.print_cate(co, po)

price_lowtohigh=Category.sort_l_to_h()

price_hightolow = Category.sort_h_to_l()

cat1.search(po)
