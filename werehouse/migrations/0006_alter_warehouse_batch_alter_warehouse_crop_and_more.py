# Generated by Django 5.1.4 on 2025-01-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werehouse', '0005_alter_warehouse_crop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='batch',
            field=models.TextField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='crop',
            field=models.CharField(choices=[('Wheat', 'Wheat'), ('Rice', 'Rice'), ('Corn', 'Corn'), ('Barely', 'Barely'), ('Oats', 'Oats'), ('Apple', 'Apple'), ('Oranges', 'Oranges'), ('Bananas', 'Bananas'), ('Grapes', 'Grapes'), ('Strawberries', 'Strawberries'), ('Tomatoes', 'Tomatoes'), ('Carrots', 'Carrots'), ('Okra', 'Okra'), ('Onions', 'Onions')], default='Wheat', max_length=255),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='storage_condition',
            field=models.CharField(choices=[('Standarad Storage Plan', 'Standarad Storage Plan'), ('Premium Storage Plan', 'Premium Storage Plan'), ('Climate-Controlled Storage Plan', 'Climate-Controlled Storage Plan')], default='climate', max_length=255),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='storage_location',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3')], default='A1', max_length=255),
        ),
    ]
