# Generated by Django 4.2.6 on 2023-11-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_author_alter_blog_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['age', 'firstname'], 'verbose_name': 'ega', 'verbose_name_plural': 'egalar'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['id'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Bloglar'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
