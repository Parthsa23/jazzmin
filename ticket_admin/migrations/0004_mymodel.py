# Generated by Django 4.1.6 on 2023-02-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_admin', '0003_remove_order_order_date_alter_route_destination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
