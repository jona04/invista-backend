# Generated by Django 4.1.2 on 2022-10-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_servico_valor_total_alter_chapa_estoque_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="servico",
            old_name="valor_total",
            new_name="valor_total_servico",
        ),
        migrations.AddField(
            model_name="nota",
            name="valor_total_nota",
            field=models.FloatField(blank=True, default=0.0, verbose_name="Total"),
        ),
    ]