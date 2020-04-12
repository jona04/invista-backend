from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Chapa,Cliente,Nota,Servico

def index(request):
    return HttpResponse("Hello, world. You're at the core index.")

# Create your views here.
def listaChapas(request):
    chapas = Chapa.objects.all()

    context = {
        'chapas':chapas
    }
    return render(request,'lista_chapas.html',context)


def home(request):
    chapas = Chapa.objects.all()
    cliente = Cliente.objects.all()
    nota = Nota.objects.all()
    servico = Servico.objects.all()
    context = {}
    context['chapas'] = chapas
    context['cliente'] = cliente
    context['nota'] = nota
    context['servico'] = servico

    return render(request, 'home.html', context)

def notas(request):
    notas = Nota.objects.all()
    paginator = Paginator(notas, 20)  # Show 20 contacts per page.
    # context = {}
    # context['notas'] = notas

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'notas.html', {'page_obj': page_obj})

    # return render(request, 'notas.html', context)
def get_number(request):
    print("number")

def nota_especifica(request,id):
    nota = Nota.objects.get(pk=id)
    servicos = nota.servico.all()
    context = {}
    context['nota'] = nota
    context['servicos'] = servicos

    return render(request,'nota_especifica.html',context)

def chapas(request):
    chapas = Chapa.objects.all()
    paginator = Paginator(chapas, 20)  # Show 20 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'chapas.html', {'page_obj': page_obj})

def clientes(request):
    clientes = Cliente.objects.all()
    paginator = Paginator(clientes, 20)  # Show 20 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'clientes.html', {'page_obj': page_obj})

def cliente_especifico(request,id):
    cliente = Cliente.objects.get(pk=id)
    context = {}
    context['cliente'] = cliente

    return render(request,'cliente_especifico.html',context)


def lista_servicos_cliente(request,id):
    cliente = Cliente.objects.get(pk=id)
    servicos = Servico.objects.filter(cliente=id)
    context = {}
    context['cliente'] = cliente
    context['servicos'] = servicos

    return render(request,'lista_servicos_cliente.html',context)

def lista_notas_cliente(request,id):
    cliente = Cliente.objects.get(pk=id)
    notas = Nota.objects.all()
    context = {}
    context['cliente'] = cliente
    context['notas'] = notas

    return render(request,'lista_notas_cliente.html',context)

def servicos(request):
    servico = Servico.objects.all()
    paginator = Paginator(servico, 20)  # Show 20 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'servicos.html', {'page_obj': page_obj})

def busca_nota(request):
    query = request.POST['campo_busca']
    notas = Nota.objects.filter(Q(id__icontains=int(query)-1000))
    paginator = Paginator(notas, 20)  # Show 20 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'notas.html', {'page_obj': page_obj})

def busca_cliente(request):
    query = request.POST['campo_busca']
    clientes = Cliente.objects.filter(Q(nome__icontains=query))
    paginator = Paginator(clientes, 20)  # Show 20 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'clientes.html', {'page_obj': page_obj})

def busca_servico(request):
    query = request.POST['campo_busca']
    servicos = Servico.objects.filter(Q(nome__icontains=query) | Q(cliente__nome__icontains=query))
    paginator = Paginator(servicos, 20)  # Show 20 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'servicos.html', {'page_obj': page_obj})