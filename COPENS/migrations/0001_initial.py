# Generated by Django 2.0.7 on 2018-07-20 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoNLLU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=200)),
                ('sense', models.CharField(max_length=200)),
                ('rel', models.CharField(max_length=200)),
                ('dep', models.CharField(max_length=200)),
                ('words', models.CharField(max_length=200)),
            ],
        ),
    ]
