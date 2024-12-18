# Generated by Django 5.1.1 on 2024-12-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0003_alter_tcc_data_inicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]