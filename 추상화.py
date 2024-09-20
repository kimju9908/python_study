# 추상화: 실체화가 되지 않는 부모로 부터 상속 받는 것
# 부모 클래스내에 이름만 선언되고 구현부가 없는 추상 메서드를 포함
# 상속 받은 클래스는 반드시 추상 메서드에 대해서 구현 해줘야 함

from abc import * # 추상클래스를 사용하기 위해 import

from dill.logger import adapter
from jupyter_client.adapter import adapt


class NetworkAdapter(metaclass=ABCMeta): # 해당 클래스를 추상클래스로 만듬
    @abstractmethod
    def connect(self):
        pass
class WiFi(NetworkAdapter):
    def __init__(self,company):
        self.company= company
    def connect(self):
        print(f"{self.company}의 wifi에 연결 되었습니다.")

class FiveG(NetworkAdapter):
    def __init__(self,company):
        self.company= company

    def connect(self):
        print(f"{self.company}의 5g에 연결 되었습니다.")
class Lte(NetworkAdapter):
    def __init__(self,company):
        self.company= company
    def connect(self):
        print(f"{self.company}의 lte에 연결 되었습니다.")

net = input("연결할 네트워크 [1]WiFi [2]5G [3]Lte: ")

if net == 1 : 
    adapter =WiFi("Kt Megapass0")
    adapter.connect()
elif net == 2:
    adapter = FiveG("SK Telecom")
    adapter.connect()
elif net == 3:
    adapter = Lte("Lg u+")
    adapter.connect()
else:
    print("연결할 프로그램이없습니다.")
