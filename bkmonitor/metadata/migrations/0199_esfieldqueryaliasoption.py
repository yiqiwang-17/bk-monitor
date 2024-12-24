# Generated by Django 3.2.15 on 2024-12-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('metadata', '0198_esstorage_archive_index_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='ESFieldQueryAliasOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='创建者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updater', models.CharField(max_length=64, verbose_name='更新者')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('table_id', models.CharField(max_length=128, verbose_name='结果表名')),
                ('field_path', models.CharField(max_length=256, verbose_name='原始字段路径')),
                ('query_alias', models.CharField(max_length=256, verbose_name='查询别名')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否已删除')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
