from django.contrib import admin, messages
from django.utils import timezone
from django.shortcuts import render

from django.contrib.admin import DateFieldListFilter

from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.

from .models import Cliente, Chapa, Servico, Nota, GrupoNotaServico, GrupoClienteNota
from datetime import date

admin.site.disable_action("delete_selected")


def imprimir_recibo2(self, request, queryset):
    if len(queryset) == 1:
        obj = queryset[0]

        data_atual = date.today()
        dia = data_atual.day
        mes = data_atual.month
        ano = data_atual.year

        id = 1000 + obj.id
        rua = obj.numero
        numero = obj.servico.cliente.bairro
        bairro = obj.servico.cliente.bairro
        cidade = obj.servico.cliente.cidade
        estado = obj.servico.cliente.estado

        if cidade is None:
            cidade = ""
        if estado is None:
            estado = ""
        if rua is None:
            rua = ""
        if numero is None:
            numero = ""
        if bairro is None:
            bairro = ""

        endereco = rua + ", " + str(numero)
        desconto = 0
        # if obj.desconto == None:
        #     desconto = 0
        # else:
        #     desconto = obj.desconto

        context = {
            "nome": obj.nome,
            "cliente": obj.servico.cliente.nome,
            "email": obj.servico.cliente.email,
            "telefone": obj.servico.cliente.telefone,
            "chapa": obj.servico.chapa.nome,
            "quantidade": obj.servico.quantidade,
            "valor_unidade": obj.servico.chapa.valor,
            "obs": obj.obs,
            "dia": dia,
            "mes": mes,
            "ano": ano,
            "id": id,
            "endereco": endereco,
            "cidade": cidade,
            "estado": estado,
            "bairro": bairro,
            "desconto": desconto,
            "valor_total": obj.servico.quantidade * obj.servico.chapa.valor,
        }
        return render(request, "layout_recibo.html", context)
        # send_mail_template(subject, template_name, context, [obj.email])

        # send_mail(
        # 	subject="Orcamento THE Brindes",
        # 	message="Mensagem do orçamento",
        # 	from_email=settings.DEFAULT_FROM_EMAIL,
        # 	recipient_list=[obj.email]
        # 	)
        type_messages = messages.INFO
        message = "Nota de entrega enviado com sucesso para %s" % obj.cliente.nome

        print("Ok")
        obj.status = 4
        obj.fineshed_at = timezone.now()
        obj.save()

    elif len(queryset) > 1:

        obj = queryset[0]

        id = 1000 + obj.id
        rua = obj.cliente.rua
        numero = obj.cliente.numero
        bairro = obj.cliente.bairro
        cidade = obj.cliente.cidade
        estado = obj.cliente.estado

        if cidade is None:
            cidade = ""
        if estado is None:
            estado = ""
        if rua is None:
            rua = ""
        if numero is None:
            numero = ""
        if bairro is None:
            bairro = ""

        data_atual = date.today()
        dia = data_atual.day
        mes = data_atual.month
        ano = data_atual.year

        total = 0
        desconto = 0
        for i in queryset:
            total = total + (i.chapa.valor * i.quantidade)

            if i.desconto is None:
                desconto = desconto + 0
            else:
                desconto = desconto + i.desconto

        total = total - desconto
        endereco = rua

        context = {
            "nome": obj.nome,
            "cliente": obj.cliente.nome,
            "email": obj.cliente.email,
            "telefone": obj.cliente.telefone,
            "chapa": obj.chapa.nome,
            "quantidade": obj.quantidade,
            "valor_unidade": obj.chapa.valor,
            "obs": obj.obs,
            "dia": dia,
            "mes": mes,
            "ano": ano,
            "id": id,
            "endereco": endereco,
            "cidade": cidade,
            "estado": estado,
            "bairro": bairro,
            "desconto": desconto,
            "valor_total": total,
            "todos": queryset,
        }

        return render(request, "layout_recibo_muitos.html", context)

        type_messages = messages.INFO
        message = "Nota de entrega enviado com sucesso para %s" % obj.cliente.nome

        print("Ok")
        obj.status = 4
        obj.fineshed_at = timezone.now()
        obj.save()

    self.message_user(request, message, type_messages)


def listar(self, request, queryset):

    list_query = []
    for i, query in enumerate(queryset):
        nota = queryset[i]
        for obj in nota.servico.all():
            id = 1000 + nota.id

            context = {
                "cliente": obj.cliente.nome,
                "nome": obj.nome,
                "id": id,
                "valor_total": obj.quantidade * obj.chapa.valor,
                "chapa": obj.chapa.nome,
                "quantidade": obj.quantidade,
                "valor_unidade": obj.chapa.valor,
                "todos": nota.servico.all(),
            }
        list_query.append(context)

    new_context = {"lista": list_query}
    return render(request, "layout_listar.html", new_context)


def imprimir_recibo(self, request, queryset):
    if len(queryset) == 1:
        nota = queryset[0]
        if len(nota.servico.all()) > 1:

            for obj in nota.servico.all():

                id = 1000 + nota.id
                rua = obj.cliente.rua
                numero = obj.cliente.numero
                bairro = obj.cliente.bairro
                cidade = obj.cliente.cidade
                estado = obj.cliente.estado

                if cidade is None:
                    cidade = ""
                if estado is None:
                    estado = ""
                if rua is None:
                    rua = ""
                if numero is None:
                    numero = ""
                if bairro is None:
                    bairro = ""

                # data_atual = date.today()
                dia = obj.uploaded_at.day
                mes = obj.uploaded_at.month
                ano = obj.uploaded_at.year

                total = 0
                desconto = 0
                for i in nota.servico.all():
                    total = total + (i.chapa.valor * i.quantidade)

                    # if i.desconto == None:
                    #     desconto = desconto + 0
                    # else:
                    #     desconto = desconto + i.desconto

                # total = total - desconto
                endereco = rua

                context = {
                    "nome": obj.nome,
                    "cliente": obj.cliente.nome,
                    "email": obj.cliente.email,
                    "telefone": obj.cliente.telefone,
                    "chapa": obj.chapa.nome,
                    "quantidade": obj.quantidade,
                    "valor_unidade": obj.chapa.valor,
                    "obs": nota.obs,
                    "dia": dia,
                    "mes": mes,
                    "ano": ano,
                    "id": id,
                    "endereco": endereco,
                    "cidade": cidade,
                    "estado": estado,
                    "bairro": bairro,
                    "desconto": desconto,
                    "valor_total": total,
                    "todos": nota.servico.all(),
                }

                return render(request, "layout_recibo_muitos.html", context)

                type_messages = messages.INFO
                message = (
                    "Nota de entrega enviado com sucesso para %s" % obj.cliente.nome
                )

                print("Ok")

        else:
            for obj in nota.servico.all():

                # data_atual = date.today()
                # dia = data_atual.day
                dia = obj.uploaded_at.day
                mes = obj.uploaded_at.month
                ano = obj.uploaded_at.year

                id = 1000 + nota.id
                rua = obj.cliente.numero
                numero = obj.cliente.bairro
                bairro = obj.cliente.bairro
                cidade = obj.cliente.cidade
                estado = obj.cliente.estado

                if cidade is None:
                    cidade = ""
                if estado is None:
                    estado = ""
                if rua is None:
                    rua = ""
                if numero is None:
                    numero = ""
                if bairro is None:
                    bairro = ""

                endereco = rua
                # desconto = 0
                # if obj.desconto == None:
                #     desconto = 0
                # else:
                #     desconto = obj.desconto

                context = {
                    "nome": obj.nome,
                    "cliente": obj.cliente.nome,
                    "email": obj.cliente.email,
                    "telefone": obj.cliente.telefone,
                    "chapa": obj.chapa.nome,
                    "quantidade": obj.quantidade,
                    "valor_unidade": obj.chapa.valor,
                    "obs": nota.obs,
                    "dia": dia,
                    "mes": mes,
                    "ano": ano,
                    "id": id,
                    "endereco": endereco,
                    "cidade": cidade,
                    "estado": estado,
                    "bairro": bairro,
                    "desconto": nota.desconto,
                    "valor_total": obj.quantidade * obj.chapa.valor,
                }
                return render(request, "layout_recibo.html", context)
                # send_mail_template(subject, template_name, context, [obj.email])

                # send_mail(
                # 	subject="Orcamento THE Brindes",
                # 	message="Mensagem do orçamento",
                # 	from_email=settings.DEFAULT_FROM_EMAIL,
                # 	recipient_list=[obj.email]
                # 	)
                type_messages = messages.INFO
                message = (
                    "Nota de entrega enviado com sucesso para %s" % obj.cliente.nome
                )

                print("Ok")

    self.message_user(request, message, type_messages)


# nome que irá aparecer no display para o osuauro
imprimir_recibo.short_description = "Imprimir Nota de Entrega"
listar.short_description = "Lista Notas"


def atualizar(self, request, queryset):
    cliente_atual = queryset[0]
    notas = Nota.objects.all()
    for nota in notas:
        try:
            if nota.servico.all()[0].cliente == cliente_atual:
                cliente_atual.nota.add(nota)
                type_messages = messages.INFO
                message = "CLiente atualizado com as notas %s" % cliente_atual
                print(nota.servico)
            else:
                type_messages = messages.INFO
                message = (
                    "Todas as notas ja estao atualizadas para esse cliente: %s"
                    % cliente_atual
                )
        except NameError:
            type_messages = messages.ERROR
            message = "Erro ao verificar nota %s" % nota
    self.message_user(request, message, type_messages)


atualizar.short_description = "Atualizar Nota"


class GrupoNotaServicoInline(admin.TabularInline):
    model = GrupoNotaServico
    extra = 1


class GrupoClienteNotaInline(admin.TabularInline):
    model = GrupoClienteNota
    extra = 1


class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", "email", "telefone", "cidade", "estado"]
    search_fields = ["nome"]
    # inlines = (GrupoClienteNotaInline,)
    actions = [atualizar]
    readonly_fields = ["nota"]


class ChapaAdmin(admin.ModelAdmin):
    list_display = ["nome", "valor", "estoque"]
    search_fields = ["nome"]


class ServicoAdmin(admin.ModelAdmin):
    list_display = ["nome", "cliente", "chapa", "quantidade", "created_at"]
    search_fields = ["nome", "cliente__nome", "created_at"]
    # actions = [imprimir_recibo]

    list_filter = (("created_at", DateFieldListFilter),)


class NotaAdmin(admin.ModelAdmin):
    exclude = ("numero",)

    list_display = ["id", "numero", "status", "created_at"]
    search_fields = ["id", "servico__cliente__nome", "created_at"]
    actions = [imprimir_recibo, listar]

    list_filter = (("created_at", DateRangeFilter),)
    inlines = (GrupoNotaServicoInline,)


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Chapa, ChapaAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Nota, NotaAdmin)
