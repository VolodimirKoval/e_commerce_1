from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {
        'title': 'Головна сторінка',
    }
    return render(request, 'index.html', context=context)


def about(request):
    context = {
        'title': 'Про сайт',
    }
    return render(request, 'about.html', context=context)


def delivery_and_payment(request):
    context = {
        'title': 'Доставка та оплата',
    }
    return render(request, 'delivery_and_payment.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакти',
    }
    return render(request, 'contacts.html', context=context)
