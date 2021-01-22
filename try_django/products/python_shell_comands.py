"""
python manage.py shell

from products.models import Product
Product.objects.all()
Product.objects.create(title='product 2 name', description='text2', price=300, summary='sweet)



python manage.py shell
from products.models import Product
Product.objects.get(id=1) #wybiera obiekt z id w którym ma przegláda© pliki <Product: Product object (1)>
obj = Product.objects.get(id=1)
dir(obj) - wszystko co mozna zrobic z modelem
obj.title -> New product
    """
