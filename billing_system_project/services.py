from billing_app.models import Product,Purchase,PurchaseItem
from decimal import Decimal,ROUND_DOWN
from django.db import transaction
from django.core.exceptions import ValidationError

def calculate_change_distribution(change_amount,denominations):
    distribution ={}
    for value_str in sorted(denominations.keys(),reverse=True):
        value = int(value_str)
        available_amount = int(denominations[value_str])
        required_amount = int(change_amount // value)

        if required_amount > 0:
            used_amount  = min(required_amount,available_amount)
            distribution[value] = used_amount
            change_amount -= (value * used_amount)

    if change_amount !=0:
        raise Exception("Unable to provide exact change")

    return distribution

@transaction.atomic
def process_bill(email, products, paid_amount, denominations):
    total_without_tax = Decimal('0.00')
    total_tax = Decimal('0.00')
    items = []

    for item in products:
        product = Product.objects.get(product_id=item["product_id"])
        quantity = int(item['quantity'])

        if quantity <= 0:
            raise Exception(f"Insufficient quantity for product: {product.name}")
        
        Purchase_price = product.unit_price * quantity
        tax_amount = Purchase_price * (product.tax_percentage /100)

        total_without_tax = total_without_tax + Purchase_price
        total_tax = total_tax + tax_amount

        product.available_stock = product.available_stock - quantity
        product.save()

        items.append((product,quantity))

    net_price_amount = total_without_tax + total_tax
    rounded_net_price = net_price_amount.quantize(Decimal('1.'),rounding=ROUND_DOWN)

    print("Total:", total_without_tax)
    print("Tax:", total_tax)
    print("Rounded:", rounded_net_price)
    print("Paid:", paid_amount)

    if paid_amount < rounded_net_price:
        raise ValidationError("Insufficient Amount Paid")
    
    balance_amount = paid_amount - rounded_net_price

    purchase = Purchase.objects.create(
        customer_email = email,
        total_without_tax = total_without_tax,
        total_tax = total_tax,
        net_price = net_price_amount,
        rounded_net_price = rounded_net_price,
        paid_amount = paid_amount,
        balance_amount = balance_amount
    )

    for item in items:
        PurchaseItem.objects.create(
            purchase = purchase,
            product = product,
            quantity = quantity,
            unit_price = product.unit_price,
            tax_percentage = product.tax_percentage
        )   


    distribution = calculate_change_distribution(balance_amount,denominations)

    return purchase, distribution