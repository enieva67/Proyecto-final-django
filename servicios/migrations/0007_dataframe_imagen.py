# Generated by Django 4.1.3 on 2022-12-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0006_dataframe'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataframe',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='servicios'),
        ),
    ]