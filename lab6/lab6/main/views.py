from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from .models import Bank, Clients, Sotrudnik, Credit, Dolzhnost, Count
from .forms import ClientsForm, SotrudnikiForm, PoseschenieForm, DolzhnostForm, CountForm, CreditForm, LoginUserForm, \
    RegisterUserForm


def index(request):
    bank = Bank.objects.all()
    client = Clients.objects.all()
    sotrudnik = Sotrudnik.objects.all()
    credit = Credit.objects.all()
    dolzhnost = Dolzhnost.objects.all()
    count = Count.objects.all()
    return render(request, 'main/index.html', {'bank': bank, 'client': client, 'sotr': sotrudnik, 'credit': credit,
                                               'dolzh': dolzhnost, 'count': count, 'role': get_role(request.user)})


def create(request):
    return render(request, 'main/create.html', {'role': get_role(request.user)})

def mainPage(request):
    return render(request, 'main/main.html', {'role': get_role(request.user)})


def clients(request):
    error=''
    form = ClientsForm()
    data = {
        'form':form,
        'error':error
    }
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверное заполнение данных'

    return render(request, 'main/clients.html', data)


def credit(request):
    error = ''
    form = CreditForm()
    data = {
        'form': form,
        'error': error
    }
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверное заполнение данных'

    return render(request, 'main/credit.html', data)


def count(request):
    error = ''
    form = CountForm()
    data = {
        'form': form,
        'error': error
    }
    if request.method == 'POST':
        form = CountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверное заполнение данных'

    return render(request, 'main/count.html', data)


def dolzhnosti(request):
    error = ''
    form = DolzhnostForm()
    data = {
        'form': form,
        'error': error
    }
    if request.method == 'POST':
        form = DolzhnostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверное заполнение данных'

    return render(request, 'main/dolzhnosti.html', data)


def poseschenie(request):
    error = ''
    form = PoseschenieForm()
    data = {
        'form': form,
        'error': error
    }
    if request.method == 'POST':
        form = PoseschenieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверное заполнение данных'

    return render(request, 'main/poseschenie.html', data)


def sotrudniki(request):
    error = ''
    form = SotrudnikiForm()
    data = {
        'form': form,
        'error': error
    }
    if request.method == 'POST':
        form = SotrudnikiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверное заполнение данных'

    return render(request, 'main/sotrudniki.html', data)


def delete_bank(request, pk):
    bank = Bank.objects.get(pk=pk)
    bank.delete()
    bank_new = Bank.objects.all()
    return render(request, 'main/index.html', {'bank': bank_new})

def delete_client(request, pk):
    client = Clients.objects.get(pk=pk)
    client.delete()
    client_new = Clients.objects.all()
    return render(request, 'main/index.html', {'client': client_new})

def delete_sotr(request, pk):
    sotr = Sotrudnik.objects.get(pk=pk)
    sotr.delete()
    sotr_new = Sotrudnik.objects.all()
    return render(request, 'main/index.html', {'sotr': sotr_new})

def delete_credit(request, pk):
    credit = Credit.objects.get(pk=pk)
    credit.delete()
    credit_new = Credit.objects.all()
    return render(request, 'main/index.html', {'credit': credit_new})

def delete_count(request, pk):
    count = Count.objects.get(pk=pk)
    count.delete()
    count_new = Count.objects.all()
    return render(request, 'main/index.html', {'count': count_new})

def delete_dolzh(request, pk):
    dolzh = Dolzhnost.objects.get(pk=pk)
    dolzh.delete()
    dolzh_new = Dolzhnost.objects.all()
    return render(request, 'main/index.html', {'dolzh': dolzh_new})

class redact_bank(UpdateView):
    model = Bank
    template_name = 'main/poseschenie.html'
    fields = ['id', 'surname', 'name', 'date_and_time', 'service', 'sotrudnik']

class redact_client(UpdateView):
    model = Clients
    template_name = 'main/clients.html'
    form_class = ClientsForm



class redact_sotr(UpdateView):
    model = Sotrudnik
    template_name = 'main/sotrudniki.html'
    form_class = SotrudnikiForm


class redact_credit(UpdateView):
    model = Credit
    template_name = 'main/credit.html'
    fields = ['id', 'client', 'summa', 'procent', 'years']

class redact_count(UpdateView):
    model = Count
    template_name = 'main/count.html'
    fields = ['id', 'client', 'summa']

class redact_dolzh(UpdateView):
    model = Dolzhnost
    template_name = 'main/dolzhnosti.html'
    fields = ['id', 'name', 'sotrudnik']

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registr.html'
    success_url = reverse_lazy('registr')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/auth.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('auth')


def get_role(user):
    template = ""
    if user.is_authenticated:
        if user.is_superuser:
            template = "admins"
        else:
            template = "users"
    return template