# Generated by Django 4.2.6 on 2023-10-26 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentId', models.AutoField(primary_key=True, serialize=False)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
