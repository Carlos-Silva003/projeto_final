# Generated by Django 5.1.1 on 2024-11-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0001_initial'),
        ('app_tcc', '0003_remove_aluno_status_aluno_ativo_aluno_curso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcc',
            name='autores',
            field=models.ManyToManyField(limit_choices_to={'ativo': True}, to='app_tcc.aluno'),
        ),
    ]
