# Generated by Django 3.0.2 on 2020-02-04 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Список категорий',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Параметр товара',
                'verbose_name_plural': 'Список параметров товаров',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Список товаров',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Список магазинов',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Parameter')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Product')),
            ],
            options={
                'verbose_name': 'Характеристики товара',
                'verbose_name_plural': 'Список характеристик товаров',
            },
        ),
        migrations.CreateModel(
            name='PriceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cost', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Product')),
            ],
            options={
                'verbose_name': 'Позиция прайс-листа',
                'verbose_name_plural': 'Список позиций прайс-листов',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price_items', models.ManyToManyField(to='app.PriceItem')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Store')),
            ],
            options={
                'verbose_name': 'Прайс-лист',
                'verbose_name_plural': 'Прайс-листы',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cost', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Product')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Список позиций заказов',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'новый'), ('processing', 'обработка'), ('executed', 'выполнен'), ('error', 'ошибка')], default='new', max_length=255)),
                ('order_items', models.ManyToManyField(to='app.OrderItem')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Список заказов',
                'ordering': ('-date',),
            },
        ),
    ]
