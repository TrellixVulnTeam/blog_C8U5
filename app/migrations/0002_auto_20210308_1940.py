# Generated by Django 3.1.7 on 2021-03-08 13:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=222, null=True)),
                ('slug', models.SlugField()),
                ('content', tinymce.models.HTMLField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
    ]
