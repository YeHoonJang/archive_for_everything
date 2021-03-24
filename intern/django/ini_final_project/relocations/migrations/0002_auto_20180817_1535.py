# Generated by Django 2.1 on 2018-08-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relocations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='content_author',
            field=models.CharField(default='anonymous', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contents',
            name='content_file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]