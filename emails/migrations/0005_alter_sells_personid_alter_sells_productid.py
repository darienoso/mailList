# Generated by Django 4.0.4 on 2022-05-10 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0004_rename_id_sells_sellid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sells',
            name='personId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sells', to='emails.persons'),
        ),
        migrations.AlterField(
            model_name='sells',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sells', to='emails.products'),
        ),
    ]
