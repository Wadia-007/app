# Generated by Django 4.0.3 on 2022-03-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_meta_desc_post_meta_tag_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_text',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]