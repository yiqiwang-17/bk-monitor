# Generated by Django 3.2.15 on 2024-12-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('metadata', '0205_rename_esstorageclusterrecord_storageclusterrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='resulttable',
            name='bk_biz_id_alias',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='业务ID别名'),
        ),
    ]
