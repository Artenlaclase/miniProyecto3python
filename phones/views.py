from lib2to3.fixes.fix_input import context
from tempfile import template

from .models import Manufacturer
from django.shortcuts import render, redirect
from .forms import SmartphoneForm, CompaniesForms

import requests

def manufacturers_index(request):
    manufacturers = Manufacturer.objects.all()
    context = {'manufacturers': manufacturers}
    return render(request, 'phones/manufacturers.html', context)


def smartphone_create(request):
    if request.method == 'POST':
        form = SmartphoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manufacturers')
    else:
        form = SmartphoneForm()
    context = {'form': form}
    return render(request, 'phones/smartphone_create.html', context)


def register_companies(request):
    if request.method == "POST":
        quantity = request.POST.dict()["companies"]

        response = requests.get(f"https://fakerapi.it/api/v1/companies?_quantity={quantity}")

        print(response.json()["data"])

        for company in response.json()["data"]:
            manufacturer = Manufacturer(
                name=company["name"],
                country=company["country"],
                date_founded=company["contact"]["birthday"],
                webpage=company["website"],
            )

            manufacturer.full_clean()
            manufacturer.save()

        return redirect("manufacturers")
    else:
        form = CompaniesForms()


    context = {
        'form': form
    }

    return render(request, template_name="phones/register_companies.html", context= context)