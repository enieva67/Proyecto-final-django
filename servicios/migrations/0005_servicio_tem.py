# Generated by Django 4.1.3 on 2022-12-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_alter_servicio_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='tem',
            field=models.CharField(max_length=50, null=True),
        ),
    ]