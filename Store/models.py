from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = (
    ("Television", "Television"),
    ("Refrigerator", "Refrigerator"),
    ("Air-Conditioner", "Air-Conditioner"),
    ("Washing-Machine","Washing-Machine")
)
    COMPANY_CHOICES = (
    ("Sony", "Sony"),
    ("Lg", "Lg"),
    ("Panasonic", "panasonic"),
    ("Samsung","Samsung"),
    ("Ifb","Ifb")
)
    
    COLOR_CHOICES = (
    ("Black", "Black"),
    ("Silver", "Silver"),
    ("Blue", "Blue")
)
   



    name = models.CharField(max_length=200,blank=False,null=False,unique=True)
    product_desc = models.CharField(max_length=500,blank=False,null=False)
    available_quantity = models.PositiveIntegerField(blank=False,null=False)
    category = models.CharField(choices=CATEGORY_CHOICES,blank=False,null=False,max_length=50)
    company = models.CharField(choices=COMPANY_CHOICES,blank=False,null=False,max_length=50)
    color = models.CharField(choices=COLOR_CHOICES,blank=False,null=False,max_length=50)
    price = models.IntegerField(blank=False,null=False)
    image =models.FileField(upload_to="Product_Images",blank=False,null=False)
    image1 =models.FileField(upload_to="Product_Images",blank=True,null=True)
    image2 =models.FileField(upload_to="Product_Images",blank=True,null=True)
    image3 =models.FileField(upload_to="Product_Images",blank=True,null=True)
    video = models.FileField(upload_to="Product_Images",blank=True,null=True)


    


    def __str__(self):
        return self.name + "  Color: " +self.color+ "  Company: "+ self.company + "  Quantity: "+ str(self.available_quantity) + "  Price: "+ str(self.price)
