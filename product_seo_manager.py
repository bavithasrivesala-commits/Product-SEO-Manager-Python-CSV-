import csv
class Product:
    def __init__(self,product,category,features):
        self.product=product
        self.category=category
        self.features=features
    def save_as_csv(self):
        with open('seo.csv',mode='a',newline='') as f:
            w=csv.writer(f)
            t=self.title()
            d=self.description()
            if f.tell() == 0:
                w.writerow(['Product', 'Category', 'Features', 'SEO Title', 'Description'])
            w.writerow([self.product,self.category,self.features,t,d])
    def view_products(self):
        with open('seo.csv','r') as k:
            r=csv.reader(k)
            data=list(r)
            header=data[0]
            rows=data[1:]
            for row in rows:
                print(f'{row[0]}-{row[1]}-{row[2]}')
            need=input('Do you need seo for any of these products:').lower()
            if need=='yes':
                seo=input('For which product do you need seo:')
                for row in rows:
                    if seo==row[0]:
                        print('Title:',row[3])
                        print('Description:',row[4])
                        break
            else:
                pass
    def title(self):
        return f'Women {self.product} {self.category}-comfortable and stylish'
    def description(self):
        return f'Upgrade your fashion with this super trendy {self.product} {self.category} which have features like {self.features}'
for i in range(1,6):
    name=input('Enter name of the product:')
    category=input('Enter category of the product:')
    features=input('Enter their features:')
    p=Product(name,category,features)
    p.save_as_csv()
p.view_products()