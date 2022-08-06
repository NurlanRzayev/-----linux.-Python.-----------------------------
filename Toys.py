class Toys:

    def __init__(self,n,k,r,p):
        self.name=n
        self.amount=k
        self.rating=r
        self.price=p
    def toys_rating_1_3(self):
        if self.rating==(1,3):
            print(self.name)
    def most_expensive(self):
        price.append((self.name,self.price))
    def x_prices_in_rating_a_b(self,x,a,b):
        if self.price<=x and self.rating==(a,b):
            print(self.name)

t1=Toys('Barby',30,(5,11),15)
t2=Toys('Soft toy',50,(1,3),8)
t3=Toys('Мachine',10,(1,3),10)

print('Toys in rating 1-3:')
t1.toys_rating_1_3()
t2.toys_rating_1_3()
t3.toys_rating_1_3()
print()

price=[]
t1.most_expensive()
t2.most_expensive()
t3.most_expensive()
price.sort(key=lambda i:i[1])
print('Most expensive toy:',price[-1][0],',','price:',price[-1][1])
print()

x=int(input('Max price: '))
a=int(input('Ratint from age: '))
b=int(input('to: '))
t1.x_prices_in_rating_a_b(x,a,b)
t2.x_prices_in_rating_a_b(x,a,b)
t3.x_prices_in_rating_a_b(x,a,b)