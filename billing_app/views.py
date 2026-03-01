from django.shortcuts import render

# Create your views here.

def billing_page(request):
    return render(request,'billing_form.html')

def generate_bill(request):
    return render(request,'generate_bill.html')

def customer_purchases(request):
    return render(request,'purchase_list.html')