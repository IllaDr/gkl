class Widget ():
    def __init__(self,text,x,y):
        self.text=text
        self.x=x
        self.y=y


    def print_info(self):
        print(f"Напис: {self.text}")
        print(f"Розташування: {self.x} {self.y}")

class Button(Widget):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.is_cliked=False
    
    def click (self):
        self.is_cliked=True
        print("Ви зареєстровані")


q=Button("Брати участь",100,100)
q.print_info()
qwestion=input("Хоче зареєструватися?  (так  /  ні):").lower()

if qwestion=="так":
    q.click()
else:
    print("А шкода!")