# Generated by Django 3.2.9 on 2021-11-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=8)),
            ],
        ),
    ]
