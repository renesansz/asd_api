# Generated by Django 3.2.2 on 2021-05-06 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('updated_at', models.DateTimeField(verbose_name='updated at')),
                ('entry_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manifesto.entrytype')),
            ],
        ),
    ]
