# Generated by Django 2.2 on 2019-04-23 10:00

import cartoview.fields
import cartoview.layers.validators
import cartoview.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_resource', '0001_initial'),
        ('app_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField(verbose_name='App Store URL')),
                ('is_default', models.BooleanField(default=False)),
                ('server_type', models.CharField(choices=[('Exchange', 'Exchange'), ('Geoserver', 'Geoserver'), ('QGISServer', 'QGISServer')], default='Geoserver', max_length=256)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='AppType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_resource.BaseModel')),
                ('name', models.CharField(default='No Name Provided', max_length=255)),
                ('extent', cartoview.fields.ListField(default=[0, 0, 0, 0], validators=[cartoview.validators.ListValidator(max_length=4, min_length=4)])),
                ('projection', models.CharField(max_length=30, validators=[cartoview.layers.validators.validate_projection])),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('base_resource.basemodel',),
        ),
        migrations.CreateModel(
            name='AppInstance',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_resource.BaseModel')),
                ('config', jsonfield.fields.JSONField(blank=True, default=dict, null=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='app_manager.App')),
            ],
            bases=('base_resource.basemodel',),
        ),
    ]
