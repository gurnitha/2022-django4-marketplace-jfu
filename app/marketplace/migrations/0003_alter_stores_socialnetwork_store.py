# Generated by Django 4.0 on 2022-02-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_alter_categories_icon_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='socialnetwork_store',
            field=models.TextField(),
        ),
    ]
