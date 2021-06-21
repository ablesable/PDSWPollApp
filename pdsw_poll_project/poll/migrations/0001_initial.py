# Generated by Django 3.1.7 on 2021-06-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('first_option', models.CharField(max_length=40)),
                ('second_option', models.CharField(max_length=40)),
                ('third_option', models.CharField(max_length=40)),
                ('first_option_count', models.IntegerField(default=0)),
                ('second_option_count', models.IntegerField(default=0)),
                ('third_option_count', models.IntegerField(default=0)),
            ],
        ),
    ]