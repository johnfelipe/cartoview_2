# Generated by Django 2.2 on 2019-04-15 12:08

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('base_resource', '0007_auto_20190415_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='keywords',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='TaggedResource',
        ),
    ]