from django.shortcuts import render
from billing_app.models import Product,Purchase,PurchaseItem
from billing_app.tasks import send_invoice_confirmation_mail

# Create your views here.

def billing_page(request):
    denominations = [500, 50, 20, 10, 5, 2, 1]
    return render(request,'billing_form.html', {'denominations': denominations})

def generate_bill(request):
    if request.method == "POST":
        email = request.POST.get("customer_email")
        paid_amount = float(request.POST.get("paid_amount"))

        product_ids = request.POST.getlist("product_id")
        quantities = request.POST.getlist("quantity")
        
        products = {}
        for product in range(len(product_ids)):
            products.append(
                {
                'product_id':product_ids[product],
                'quantity' : quantities[product]
                 }
            )

        send_invoice_confirmation_mail.delay(products,email)

    return render(request,'generate_bill_result.html')

def customer_purchases(request):
    email = request.GET.get('email')
    purchases = Purchase.objects.filter(customer_email = email)
    return render(request,'purchase_list.html',{'purchases': purchases})

def purchase_detail(request, pk):
    purchase = Purchase.objects.get(id=pk)
    purchase_items = PurchaseItem.objects.filter(purchase=purchase)
    return render(request,'purchase_detail.html',{'purchase': purchase, 'purchase_items': purchase_items})