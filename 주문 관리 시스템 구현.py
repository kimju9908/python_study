import decimal

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = decimal.Decimal(price)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Order:
    def __init__(self):
        self.products = []
        self.total = decimal.Decimal(0)

    def add_item(self, product):
        self.products.append(product)
        self.total += product.get_price()

    def get_item(self, name):
        for product in self.products:
            if product.get_name() == name:
                return product
        return None

    def remove_item(self, name):
        for i, product in enumerate(self.products):
            if product.get_name() == name:
                del self.products[i]
                self.total -= product.get_price()
                return True
        return False

    def calculate_final_price(self):
        final_price = self.total * decimal.Decimal(1.06)
        print(f"최종 가격은 {round(final_price,2)}입니다.")

if __name__ == "__main__":
    my_order = Order()

    while True:
        num = int(input("1. 제품 추가 2. 제품 제거 3. 제품 목록 보기 4. 제품 상세보기 5. 최종 가격 계산 6. 프로그램 종료: "))
        if num == 1:
            name = input("제품의 이름을 입력하세요: ")
            price = input("제품의 가격을 입력하세요: ")
            product = Product(name, price)
            my_order.add_item(product)

        elif num == 2:
            name = input("삭제할 제품 이름: ")
            if my_order.remove_item(name):
                print(f"{name} 제품이 제거되었습니다.")
            else:
                print("제품이 없습니다.")

        elif num == 3:
            if my_order.products:
                for product in my_order.products:
                    print(f"{product.get_name()}: {product.get_price()}")
            else:
                print("주문 내역이 없습니다.")

        elif num == 4:
            name = input("상세보기할 제품을 입력하세요: ")
            product = my_order.get_item(name)
            if product:
                print(f"제품 이름: {product.get_name()}")
                print(f"제품 가격: {product.get_price()}")
            else:
                print("해당 제품이 없습니다.")
        elif num == 5:
            my_order.calculate_final_price()
        elif num == 6:
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효하지 않은 선택입니다.")
