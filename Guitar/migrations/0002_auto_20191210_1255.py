# Generated by Django 2.2.6 on 2019-12-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guitar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Guitar/funcionarios'),
        ),
        migrations.AlterField(
            model_name='guitarra',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Guitar/guitars'),
        ),
    ]