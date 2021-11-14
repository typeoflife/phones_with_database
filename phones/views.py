from django.http import HttpResponse
from django.shortcuts import render

from phones.models import Phone

def show_phones(request):
    phone_objects = Phone.objects.all()
    phones = [f'{p.id}, {p.name}, {p.price}, {p.image}, {p.release_date}, {p.lte_exists}, {p.slug}' for p in phone_objects]
    return HttpResponse('<br>'.join(phones))


def show_catalog(request):
    all_phones = Phone.objects.all()
    sort_pages = request.GET.get('sort')
    template_name = 'catalog.html'
    if sort_pages == 'low':
        all_phones = all_phones.order_by('price')
    elif sort_pages == 'high':
        all_phones = all_phones.order_by('-price')
    elif sort_pages == 'name':
        all_phones = all_phones.order_by('name')
    context = {
        'phones': all_phones,
    }
    return render(request, template_name, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug__contains=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)
