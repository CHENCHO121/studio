# Generated by Django 3.0 on 2020-06-27 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0004_auto_20200623_1728'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog_Photo',
        ),
        migrations.DeleteModel(
            name='Blog_video',
        ),
        migrations.DeleteModel(
            name='Cinematography',
        ),
        migrations.DeleteModel(
            name='Contact_Us',
        ),
        migrations.DeleteModel(
            name='Hire_Us',
        ),
        migrations.DeleteModel(
            name='Photography',
        ),
        migrations.DeleteModel(
            name='PhotoOnHomePage',
        ),
        migrations.DeleteModel(
            name='VideoOnHomePage',
        ),
    ]
