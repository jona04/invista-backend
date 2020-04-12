from django.db import models
from django.urls import reverse

class Cliente(models.Model):

    nome = models.CharField('* Nome / Empresa',max_length=200)
    email = models.EmailField('* Email',max_length=100,null=True,blank=True)
    telefone = models.CharField('* Fone',max_length=20,null=True,blank=True)
    cnpj = models.CharField('CNPJ',max_length=40,null=True,blank=True)
    cpf = models.CharField('CPF',max_length=40,null=True,blank=True)
    rua = models.CharField('Rua',max_length=40,null=True,blank=True)
    bairro = models.CharField('Bairro',max_length=40,null=True,blank=True)
    numero = models.IntegerField('Numero',null=True,blank=True)
    cidade = models.CharField('Cidade',max_length=40,null=True,blank=True)
    estado = models.CharField('Estado',max_length=40,null=True,blank=True)
    cep = models.CharField('Cep',max_length=40,null=True,blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True,null=True)
    uploaded_at = models.DateTimeField('Atualizado em', auto_now=True,null=True)
    nota = models.ManyToManyField('Nota', through='GrupoClienteNota', null=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse(
            'cliente_especifico',
            args=[self.id]
    )

    def get_list_services(self):
        return reverse(
            'lista_servicos_cliente',
            args=[self.id]
    )

    def get_list_notas(self):
        return reverse(
            'lista_notas_cliente',
            args=[self.id]
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-created_at']



class Chapa(models.Model):
    nome = models.CharField('Nome',max_length=100)
    valor = models.FloatField('Valor',null=True,blank=True)
    estoque = models.IntegerField('Quantidade em Estoque',null=True,blank=True)
    marca = models.CharField('Marca',null=True,blank=True,max_length=50)
    obs = models.CharField('Obs', max_length=255,null=True,blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    uploaded_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Chapa"
        verbose_name_plural = "Chapas"
        ordering = ['nome']

class Servico(models.Model):
    nome = models.CharField('Nome Serviço', max_length=200)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', related_name='clientes',on_delete=models.PROTECT)
    chapa = models.ForeignKey(Chapa, verbose_name='Chapa', related_name='servico', on_delete=models.PROTECT)
    quantidade = models.IntegerField('Quantidade',null=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    uploaded_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    def __str__(self):
        return self.nome

    def valor(self):
        return self.quantidade * self.chapa.valor

    class Meta:
        verbose_name = "Servico"
        verbose_name_plural = "Servicos"
        ordering = ['-created_at']


class Nota(models.Model):
    # cliente = models.ForeignKey(Cliente, verbose_name='Cliente', related_name='clientes', on_delete=models.PROTECT)
    desconto = models.FloatField('Desconto', null=True, blank=False,default=0)
    numero = models.IntegerField('Numero Nota',null=True,blank=False,default=0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    uploaded_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)
    obs = models.TextField('Observações', null=True, blank=True)
    servico = models.ManyToManyField(Servico, through='GrupoNotaServico', null=True)

    def __str__(self):
        return str(self.numero)

    STATUS_CHOICE = (
        (0, 'Em aberto'),
        (1, 'Pago'),

    )
    status = models.IntegerField('Situação', choices=STATUS_CHOICE, default=0, blank=True)

    @property
    def numero(self):
        return (self.id + 1000)

    def get_absolute_url(self):
        return reverse(
            'nota_especifica',
            args=[self.id]
    )

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        ordering = ['-created_at']


class GrupoClienteNota(models.Model):
    nota = models.ForeignKey(Nota,on_delete=models.PROTECT,null=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return str(self.cliente.nome)



class GrupoNotaServico(models.Model):
    nota = models.ForeignKey(Nota,on_delete=models.PROTECT,null=True)
    servico = models.ForeignKey(Servico,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return str(self.nota.id)

    def save(self, *args, **kwargs):
        super(GrupoNotaServico, self).save(*args, **kwargs)
        cliente = self.servico.cliente
        cliente.nota.add(self.nota)

