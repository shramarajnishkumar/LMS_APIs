# Generated by Django 4.0.6 on 2022-07-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0008_book_issues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issues',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]