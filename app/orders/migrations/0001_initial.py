# Generated by Django 4.0 on 2022-02-13 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketplace', '0003_alter_stores_socialnetwork_store'),
        ('accounts', '0004_alter_users_email_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details_order', models.CharField(max_length=100)),
                ('quantity_order', models.FloatField(default='0')),
                ('price_order', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email_order', models.CharField(max_length=100)),
                ('country_order', models.CharField(max_length=100)),
                ('city_order', models.CharField(max_length=100)),
                ('phone_order', models.CharField(max_length=100)),
                ('address_order', models.TextField()),
                ('process_order', models.TextField()),
                ('status_order', models.TextField()),
                ('date_created_order', models.DateTimeField(auto_now_add=True)),
                ('date_updated_order', models.DateTimeField(auto_now=True)),
                ('id_product_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.products')),
                ('id_store_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.stores')),
                ('id_user_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.users')),
            ],
            options={
                'verbose_name_plural': 'Orders',
                'ordering': ('status_order',),
            },
        ),
    ]
