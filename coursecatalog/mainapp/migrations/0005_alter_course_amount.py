# Generated by Django 3.2 on 2021-05-01 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='amount',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=3, verbose_name='Количество лекций'),
        ),
    ]
