# Generated by Django 4.1.2 on 2022-10-17 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_rename_valor_total_servico_valor_total_servico_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Saidas",
        ),
    ]