from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Chapa, Cliente, Nota, Servico


def index():
    return HttpResponse("Hello, world. You're at the core index.")


# Create your views here.
def listaChapas(request):
    # pylint: disable=no-member
    chapas_list = Chapa.objects.all()

    context = {"chapas": chapas_list}
    return render(request, "lista_chapas.html", context)


def home(request):
    # pylint: disable=no-member
    chapas_list = Chapa.objects.all()
    cliente = Cliente.objects.all()
    nota = Nota.objects.all()
    servico = Servico.objects.all()
    context = {}
    context["chapas"] = chapas_list
    context["cliente"] = cliente
    context["nota"] = nota
    context["servico"] = servico

    return render(request, "home.html", context)


def notas(request):
    # pylint: disable=no-member
    notas_list = Nota.objects.all()
    paginator = Paginator(notas_list, 20)  # Show 20 contacts per page.
    # context = {}
    # context['notas'] = notas

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "notas.html", {"page_obj": page_obj})

    # return render(request, 'notas.html', context)


def get_number():
    print("number")


def nota_especifica(request, newid):
    # pylint: disable=no-member
    nota = Nota.objects.get(pk=newid)
    servico_list = nota.servico.all()
    context = {}
    context["nota"] = nota
    context["servicos"] = servico_list

    return render(request, "nota_especifica.html", context)


def chapas(request):
    # pylint: disable=no-member
    chapa_list = Chapa.objects.all()
    paginator = Paginator(chapa_list, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "chapas.html", {"page_obj": page_obj})


def clientes(request):
    # pylint: disable=no-member
    cliente_list = Cliente.objects.all()
    paginator = Paginator(cliente_list, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "clientes.html", {"page_obj": page_obj})


def cliente_especifico(request, newid):
    # pylint: disable=no-member
    cliente = Cliente.objects.get(pk=newid)
    context = {}
    context["cliente"] = cliente

    return render(request, "cliente_especifico.html", context)


def lista_servicos_cliente(request, newid):
    # pylint: disable=no-member
    cliente = Cliente.objects.get(pk=newid)
    servico_list = Servico.objects.filter(cliente=newid)
    context = {}
    context["cliente"] = cliente
    context["servicos"] = servico_list

    return render(request, "lista_servicos_cliente.html", context)


def lista_notas_cliente(request, newid):
    # pylint: disable=no-member
    cliente = Cliente.objects.get(pk=newid)
    nota_list = Nota.objects.all()
    context = {}
    context["cliente"] = cliente
    context["notas"] = nota_list

    return render(request, "lista_notas_cliente.html", context)


def servicos(request):
    # pylint: disable=no-member
    servico = Servico.objects.all()
    paginator = Paginator(servico, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "servicos.html", {"page_obj": page_obj})


def busca_nota(request):
    # pylint: disable=no-member
    query = request.POST["campo_busca"]
    nota_list = Nota.objects.filter(Q(id__icontains=int(query) - 1000))
    paginator = Paginator(nota_list, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "notas.html", {"page_obj": page_obj})


def busca_cliente(request):
    # pylint: disable=no-member
    query = request.POST["campo_busca"]
    cliente_list = Cliente.objects.filter(Q(nome__icontains=query))
    paginator = Paginator(cliente_list, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "clientes.html", {"page_obj": page_obj})


def busca_servico(request):
    # pylint: disable=no-member
    query = request.POST["campo_busca"]
    servico_list = Servico.objects.filter(
        Q(nome__icontains=query) | Q(cliente__nome__icontains=query)
    )
    paginator = Paginator(servico_list, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "servicos.html", {"page_obj": page_obj})
