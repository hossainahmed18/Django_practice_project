# Generated by Django 2.0.5 on 2018-08-31 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0006_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=20),
        ),
    ]
