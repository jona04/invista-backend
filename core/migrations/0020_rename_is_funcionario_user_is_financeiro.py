# Generated by Django 4.1.2 on 2022-10-20 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_delete_saidas"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_funcionario",
            new_name="is_financeiro",
        ),
    ]
