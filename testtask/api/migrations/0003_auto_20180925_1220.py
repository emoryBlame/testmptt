# Generated by Django 2.1.1 on 2018-09-25 12:20

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180925_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='parent',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Group', verbose_name='Родитель'),
        ),
    ]