# Generated by Django 3.1.7 on 2021-04-08 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20210408_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=24)),
            ],
        ),
        migrations.DeleteModel(
            name='Navbar',
        ),
    ]