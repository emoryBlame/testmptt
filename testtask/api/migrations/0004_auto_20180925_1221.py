# Generated by Django 2.1.1 on 2018-09-25 12:21

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180925_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Group', verbose_name='Родитель'),
        ),
    ]
