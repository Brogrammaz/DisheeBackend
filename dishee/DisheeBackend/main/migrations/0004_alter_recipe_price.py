# Generated by Django 4.1.3 on 2022-12-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_remove_comment_actiate_recipe_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
