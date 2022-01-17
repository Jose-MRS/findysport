# Generated by Django 3.2.9 on 2021-12-01 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=16)),
                ('descripcion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=20)),
                ('creador', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_local', models.CharField(max_length=30)),
                ('direccion_local', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField(default=0)),
                ('direccion', models.CharField(max_length=100)),
                ('cod_postal', models.IntegerField(default=0)),
                ('ciudad', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('horas', models.CharField(max_length=30)),
                ('encargado', models.CharField(max_length=30)),
                ('espacio', models.IntegerField(default=0)),
                ('espacio_max', models.IntegerField(default=15)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findysport_app.actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_en', models.CharField(max_length=30)),
                ('actividad', models.ManyToManyField(to='findysport_app.Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Apuntado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.ManyToManyField(to='findysport_app.Actividad')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findysport_app.grupo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findysport_app.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findysport_app.local'),
        ),
    ]