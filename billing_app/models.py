from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=100)
    available_stock = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table ='Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['product_id']

    def __str__(self):
        return f"{self.name} - {self.product_id}"
    
class Purchase(models.Model):
    customer_email = models.EmailField()
    total_without_tax = models.DecimalField(max_digits=10,decimal_places=2)
    total_tax = models.DecimalField(max_digits=10,decimal_places=2)
    net_price = models.DecimalField(max_digits=10,decimal_places=2)
    rounded_net_price = models.DecimalField(max_digits =10,decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance_amount = models.DecimalField(max_digits=10,decimal_places=2)
    created_at =models.DateTimeField(auto_now_add =True)

    class Meta:
        db_table ='Purchase'
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_email} - {self.created_at}"
    

class PurchaseItem(models.Model):
        purchase = models.ForeignKey(Purchase,on_delete=models.CASCADE,related_name='items')
        product = models.ForeignKey(Product,on_delete=models.PROTECT)
        quantity = models.PositiveIntegerField()
        unit_price = models.DecimalField(max_digits=10,decimal_places=2)
        tax_percentage =models.DecimalField(max_digits=10,decimal_places=2)

        class Meta:
            db_table ='Purchase_Item'
            verbose_name ='Purchase_Item'
            verbose_name_plural = 'Purchase_Items'
            unique_together = ["purchase","product"]

        def __str__(self):
             return f"{self.product.product_id} - {self.quantity}"  