# Generated by Django 4.0 on 2022-01-25 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_creator_item_nft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='nft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.nft'),
        ),
    ]
