# Generated by Django 4.2.4 on 2023-08-10 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_question_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='respondant',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=6),
            preserve_default=False,
        ),
    ]
