# Generated by Django 2.0.2 on 2018-06-27 09:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=64, null=True, unique=True)),
                ('descricao', models.CharField(max_length=512, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128, null=True)),
                ('peso', models.IntegerField(default=0, null=True)),
                ('descricao', models.CharField(max_length=512, null=True)),
                ('quantidade', models.IntegerField(default=0, null=True)),
                ('genCodigo', models.CharField(max_length=32, null=True, unique=True)),
            ],
            options={
                'db_table': 'componentesEstrutura',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ConfigTenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=64, null=True, unique=True)),
                ('descricao', models.CharField(max_length=512, null=True)),
            ],
            options={
                'db_table': 'configTenda',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='FamiliaComponentes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128, null=True)),
                ('tag', models.CharField(max_length=32, null=True, unique=True)),
                ('descricao', models.CharField(max_length=512, null=True)),
            ],
            options={
                'db_table': 'familiaComponente',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ListaDeComponentes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField(default=0, null=True)),
                ('codigoLista', models.CharField(max_length=64, null=True)),
                ('componente', models.ForeignKey(db_column='componente_id', on_delete=django.db.models.deletion.CASCADE, to='sdp.Componente')),
            ],
            options={
                'db_table': 'ListaDeComponentes',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, default=datetime.date(2018, 6, 27))),
                ('local', models.CharField(max_length=64, null=True)),
                ('cliente', models.ForeignKey(db_column='cliente_id', on_delete=django.db.models.deletion.CASCADE, to='sdp.Cliente')),
            ],
            options={
                'db_table': 'obras',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TendaComponente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('componente', models.ForeignKey(db_column='componente_id', on_delete=django.db.models.deletion.CASCADE, related_name='pertence', to='sdp.Componente')),
                ('tenda', models.ForeignKey(db_column='tenda_id', on_delete=django.db.models.deletion.CASCADE, to='sdp.ConfigTenda')),
            ],
            options={
                'db_table': 'TendaComponente',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TipoTenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, null=True)),
                ('description', models.CharField(max_length=512, null=True)),
            ],
            options={
                'db_table': 'tipoTenda',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=64, null=True, unique=True)),
                ('username', models.CharField(max_length=64, null=True, unique=True)),
                ('password', models.CharField(max_length=64, null=True)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, null=True)),
                ('description', models.CharField(max_length=512, null=True)),
            ],
            options={
                'db_table': 'UserLevels',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.ForeignKey(db_column='level_id', on_delete=django.db.models.deletion.CASCADE, related_name='level', to='sdp.UserLevel'),
        ),
        migrations.AddField(
            model_name='configtenda',
            name='tipo',
            field=models.ForeignKey(db_column='tipoTenda_id', on_delete=django.db.models.deletion.CASCADE, to='sdp.TipoTenda'),
        ),
        migrations.AddField(
            model_name='componente',
            name='familia',
            field=models.ForeignKey(db_column='familiaComponente_id', on_delete=django.db.models.deletion.CASCADE, to='sdp.FamiliaComponentes'),
        ),
    ]
