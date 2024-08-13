from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Product, Review

import telebot


BOT_TOKEN = '6437744824:AAF9JPnmHJ6z9uXQyMCSjDkM41b0WNmOEkc'
CHAT_ID = 6318613751


bot = telebot.TeleBot(BOT_TOKEN)

# Create your views here.
def home(request):
    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(name__contains=search).all()
    else:
        products = Product.objects.all()

    return render(request, "index.html", {
        'products': products,
        'products_found': len(products) > 0,
        'search': search if search else '',
    })

def view_product(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        usage_duration = request.POST.get('duration')
        text = request.POST.get('review')

        review = Review(
            product=product,
            author=author,
            rating=rating,
            usage_duration=usage_duration,
            text=text,
        )
        review.save()

    reviews = product.review_set.all()

    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews,
    })

def payment(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        # Send message to Telegram
        bot.send_message(CHAT_ID, f'''📦 Новый заказ: {product.name}
💸 Цена: {product.price} рублей

ФИО покупателя: {name}
Адрес доставки: {address}
''')
        return redirect('/success')

    return render(request, "payment.html", {
        'product': product
    })

def success(request):
    return render(request, 'success.html')