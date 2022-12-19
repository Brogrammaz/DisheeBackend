# Generated by Django 4.1.3 on 2022-11-22 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='actiate',
        ),
        migrations.AddField(
            model_name='recipe',
            name='price',
            field=models.IntegerField(default=0, max_length=4),
        ),
    ]
