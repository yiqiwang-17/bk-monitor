# Generated by Django 3.2.15 on 2024-04-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('log_search', '0073_merge_0072_auto_20231205_1548_0072_auto_20231228_1420'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='userindexsetsearchhistory',
            index=models.Index(fields=['created_by'], name='log_search__created_04cea8_idx'),
        ),
    ]
