# Generated by Django 4.0.4 on 2022-06-08 11:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_enumfield.db.fields
import swaps.model_enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_offered', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_accepted', models.DateTimeField(blank=True, null=True)),
                ('status', django_enumfield.db.fields.EnumField(default=0, enum=swaps.model_enums.SwapStatus)),
                ('desired_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swaps_desired', to='products.product')),
                ('offered_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swaps_offered', to='products.product')),
            ],
        ),
    ]
