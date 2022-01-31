from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from sistema.forms import cadastroform
from sistema.models import cadastro
# Criei as funções para redenrizar as paginas e redirect



def home(request):
    data = {}
    all = cadastro.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = cadastroform()
    return render(request, 'form.html', data)


def create(request):
    form = cadastroform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = cadastro.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = cadastro.objects.get(pk=pk)
    data['form'] = cadastroform(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = cadastro.objects.get(pk=pk)
    form = cadastroform(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = cadastro.objects.get(pk=pk)
    db.delete()
    return redirect('home')


def sim(request):
    return render(request, 'sim.html')
