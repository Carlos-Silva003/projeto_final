# Generated by Django 5.1.2 on 2024-10-20 23:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('capa', models.ImageField(blank=True, null=True, upload_to='tcc_covers/')),
                ('descricao', models.TextField()),
                ('curso', models.CharField(max_length=100)),
                ('data_inicio', models.DateField()),
                ('data_entrega', models.DateField()),
                ('status', models.CharField(choices=[('Em Andamento', 'Em Andamento'), ('Aguardando', 'Aguardando'), ('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'), ('Concluído', 'Concluído')], default='Em Andamento', max_length=20)),
                ('autores', models.ManyToManyField(related_name='autores', to=settings.AUTH_USER_MODEL)),
                ('orientador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orientador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]