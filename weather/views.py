from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import City, TemperatureRecord
from .forms import CityForm, TemperatureRecordForm, LoginForm


# Create your views here.
def show_cities(request):
    if request.method == 'POST':
        city_form = CityForm(request.POST)
        if city_form.is_valid():
            city_form.save()
            return HttpResponseRedirect('/')
        loginform = LoginForm(request, data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        city_form = CityForm()
        login_form = LoginForm()

    try:
        cities = City.objects.all()
    except City.DoesNotexist:
        cities = []

    return render(request, 'city_list.html', {'cities': cities, 'form': city_form, 'loginform': login_form})


@login_required
def edit_city(request, id):
    record = get_object_or_404(City, pk=id)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CityForm(instance=record)
    return render(request, 'edit_city.html', {'form': form})


@login_required
def delete_city(request, id):
    city = City.objects.get(id=id)
    city.delete()
    return HttpResponseRedirect('/')


def show_temp_records(request, city_id):
    if request.method == 'POST':
        record_form = TemperatureRecordForm(request.POST)
        if record_form.is_valid():
            instance = record_form.save(commit=False)
            instance.city_id = city_id
            instance.save()
            return HttpResponseRedirect(f'/temp_records/{city_id}')
        loginform = LoginForm(request, data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user)
            return HttpResponseRedirect(f'/temp_records/{city_id}')
    else:
        record_form = TemperatureRecordForm()
        login_form = LoginForm()

    try:
        records = TemperatureRecord.objects.filter(city_id=city_id).order_by('date')
    except TemperatureRecord.DoesNotExist:
        records = []

    city = City.objects.get(id=city_id)

    return render(request, 'temp_records.html', {'records': records, 'form': record_form,
                                                 'loginform': login_form, 'city': city})


@login_required
def edit_temp_record(request, city_id, id):
    record = get_object_or_404(TemperatureRecord, pk=id)
    form = TemperatureRecordForm(request.POST, instance=record)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/temp_records/{city_id}')
    else:
        form = TemperatureRecordForm(instance=record)
    return render(request, 'edit_record.html', {'form': form, 'city_id': city_id})


@login_required
def delete_temp_record(request, city_id, id):
    record = TemperatureRecord.objects.get(id=id)
    record.delete()
    return HttpResponseRedirect(f'/temp_records/{city_id}')
