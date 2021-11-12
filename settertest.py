''' settertest.py - Pythonのプロパティsetterのテスト '''

class Car:
    ''' テスト用に車を表すクラス '''

    def __init__(self):
        
        self.__color = 'defaultcolor'
        self.__wheel = 'defaultwheel'
        self.__engine = 'defaultengine'

        return

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, col: str):
        self.__color = col
        return

    @property
    def wheel(self):
        return self.__wheel

    @wheel.setter
    def wheel(self, wh: str, en: str):
        self.__wheel = wh
        self.__engine = en
        return

    @property
    def engine(self):
        return self.__engine


# ここからメインプログラム
car = Car()

print('デフォルトのcolor')
print(car.color)

print('colorを新しく設定します。')
from termcolor import colored
car.color = colored('green', 'green')

print('新しいcolor')
print(car.color)

print('デフォルトのwheel')
print(car.wheel)

print('デフォルトのengine')
print(car.engine)

print('wheelを新しく設定します。')
# この行はエラーになる。setterを直接呼び出すのならともかく、 =演算子をつかって2つのパラメータを渡すのは不可能の模様
car.wheel = 'newwheel', 'newengine'

print('新しいwheel')
print(car.wheel)
