from django.contrib import admin,messages
from django.utils import timezone
from django.shortcuts import render

# Register your models here.

from .models import Cliente,Chapa,Servico
from datetime import date

admin.site.disable_action('delete_selected')


def imprimir_recibo(self, request, queryset):
    if (len(queryset) == 1):
        obj = queryset[0]



        data_atual = date.today()
        dia = data_atual.day
        mes = data_atual.month
        ano = data_atual.year

        id = 10000 + obj.id
        rua = obj.cliente.rua
        numero = obj.cliente.numero
        bairro = obj.cliente.bairro
        cidade = obj.cliente.cidade
        estado = obj.cliente.estado

        if cidade == None:
            cidade = ''
        if estado == None:
            estado = ''
        if rua == None:
            rua = ''
        if numero == None:
            numero = ''
        if bairro == None:
            bairro = ''

        endereco = rua + ' ' + numero + ' ' + bairro
        desconto = 0
        if obj.desconto == None:
            desconto = 0
        else:
            desconto = obj.desconto

        context = {
            'nome': obj.nome,
            'cliente': obj.cliente.nome,
            'email': obj.cliente.email,
            'telefone': obj.cliente.telefone,
            'chapa': obj.chapa.nome,
            'quantidade': obj.quantidade,
            'valor_unidade': obj.chapa.valor,
            'obs':obj.obs,
            'dia':dia,
            'mes':mes,
            'ano':ano,
            'id': id,
            'endereco': endereco,
            'cidade' : cidade,
            'estado' : estado,



            'desconto':desconto,
            'valor_total': obj.quantidade * obj.chapa.valor - desconto,

        }
        return render(request,
                      'layout_recibo.html',
                      context)
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

    self.message_user(request, message, type_messages)

#nome que irá aparecer no display para o osuauro
imprimir_recibo.short_description = "Imprimir Nota de Entrega"




class ClienteAdmin(admin.ModelAdmin):
	list_display = ['nome','email','telefone','cidade','estado']
	search_fields = ['nome']

class ChapaAdmin(admin.ModelAdmin):
	list_display = ['nome','valor','estoque']
	search_fields = ['nome']

class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome','cliente','chapa','quantidade']
    search_fields = ['nome']
    actions = [imprimir_recibo]

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Chapa,ChapaAdmin)
admin.site.register(Servico,ServicoAdmin)
