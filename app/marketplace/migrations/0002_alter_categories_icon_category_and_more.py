# Generated by Django 4.0 on 2022-02-13 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='icon_category',
            field=models.ImageField(blank=True, upload_to='products/categories/icons/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='image_category',
            field=models.ImageField(blank=True, upload_to='products/categories/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='image_subcategory',
            field=models.ImageField(blank=True, null=True, upload_to='products/subcategories/%Y/%m/%d'),
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_store', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=225, unique=True)),
                ('logo_store', models.ImageField(blank=True, null=True, upload_to='products/stores/%Y/%m/%d')),
                ('cover_store', models.ImageField(blank=True, null=True, upload_to='products/stores/%Y/%m/%d')),
                ('about_store', models.TextField()),
                ('abstract_store', models.TextField()),
                ('email_store', models.CharField(max_length=100)),
                ('country_store', models.CharField(max_length=50)),
                ('city_store', models.CharField(max_length=50)),
                ('address_store', models.TextField()),
                ('phone_store', models.CharField(max_length=50)),
                ('socialnetwork_store', models.CharField(max_length=100)),
                ('products_store', models.TextField()),
                ('date_created_store', models.DateTimeField(auto_now_add=True)),
                ('date_updated_store', models.DateTimeField(auto_now=True)),
                ('id_user_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.users')),
            ],
            options={
                'verbose_name_plural': 'Stores',
                'ordering': ('name_store',),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_product', models.TextField()),
                ('state_product', models.CharField(max_length=50)),
                ('title_list_product', models.CharField(max_length=50)),
                ('name_product', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=225, unique=True)),
                ('image_product', models.ImageField(null=True, upload_to='products/products/%Y/%m/%d, blank=True')),
                ('price_product', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_product', models.CharField(max_length=50)),
                ('stock_product', models.IntegerField(default='0')),
                ('delivery_time_product', models.IntegerField(default='0')),
                ('offer_product', models.CharField(max_length=100)),
                ('description_product', models.TextField()),
                ('summary_product', models.TextField()),
                ('details_product', models.TextField()),
                ('specifications_product', models.CharField(max_length=50)),
                ('gallery_product', models.CharField(max_length=50)),
                ('video_product', models.TextField()),
                ('top_banner_product', models.CharField(max_length=255)),
                ('default_banner_product', models.CharField(max_length=255)),
                ('horizontal_slider_product', models.TextField()),
                ('vertical_slider_product', models.TextField()),
                ('reviews_product', models.TextField()),
                ('tags_product', models.CharField(max_length=50)),
                ('sales_product', models.IntegerField(default='0')),
                ('views_product', models.IntegerField(default='0')),
                ('date_created_product', models.DateTimeField(auto_now_add=True)),
                ('date_updated_product', models.DateTimeField(auto_now=True)),
                ('id_category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.categories')),
                ('id_store_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.stores')),
                ('id_subcategory_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.subcategories')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('name_product',),
            },
        ),
    ]
