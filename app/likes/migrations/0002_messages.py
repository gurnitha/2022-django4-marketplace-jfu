# Generated by Django 4.0 on 2022-02-13 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_users_email_user'),
        ('marketplace', '0003_alter_stores_socialnetwork_store'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_message', models.TextField()),
                ('answer_message', models.TextField()),
                ('date_created_message', models.DateTimeField(auto_now_add=True)),
                ('date_updated_message', models.DateTimeField(auto_now=True)),
                ('id_product_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.products')),
                ('receiver_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.stores')),
                ('transmitter_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.users')),
            ],
            options={
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
