# Generated by Django 4.2.4 on 2023-08-10 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_alter_category_options_alter_respondant_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=9),
        ),
    ]
