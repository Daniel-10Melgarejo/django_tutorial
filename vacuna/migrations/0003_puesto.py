# Generated by Django 3.2.6 on 2021-10-01 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacuna', '0002_alter_sede_habilitado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('habilitado', models.BooleanField(default=False)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacuna.sede')),
            ],
        ),
    ]
