# Generated by Django 4.2.16 on 2024-11-14 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
    ]