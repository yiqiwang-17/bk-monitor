# Generated by Django 3.2.15 on 2023-12-28 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_search', '0071_merge_20231124_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindexset',
            name='sort_fields',
            field=models.JSONField(default=list, null=True, verbose_name='排序字段'),
        ),
        migrations.AddField(
            model_name='logindexset',
            name='target_fields',
            field=models.JSONField(default=list, null=True, verbose_name='定位字段'),
        ),
    ]
