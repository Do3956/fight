# Generated by Django 2.2.6 on 2019-10-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='status',
        ),
        migrations.AddField(
            model_name='heros',
            name='_class',
            field=models.CharField(default='', max_length=20, verbose_name='代码里对应的类名'),
        ),
        migrations.AddField(
            model_name='skills',
            name='_class',
            field=models.CharField(default='', max_length=20, verbose_name='代码里对应的类名'),
        ),
        migrations.AlterField(
            model_name='heros',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='角色名'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=20, verbose_name='技能名称'),
        ),
    ]