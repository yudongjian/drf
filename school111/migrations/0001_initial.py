# Generated by Django 2.2.17 on 2022-02-28 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tno', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='learn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='', max_length=20)),
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school111.Student')),
            ],
        ),
    ]
