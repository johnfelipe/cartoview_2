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
        ('connections', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_resource.BaseModel')),
                ('name', models.CharField(max_length=255)),
                ('bounding_box', cartoview.fields.ListField(default=[0, 0, 0, 0], validators=[cartoview.validators.ListValidator(max_length=4, min_length=4)])),
                ('projection', models.CharField(max_length=30, validators=[cartoview.layers.validators.validate_projection])),
                ('valid', models.BooleanField(default=True)),
                ('extra', jsonfield.fields.JSONField(default=dict)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='layers', to=settings.AUTH_USER_MODEL)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='layers', to='connections.Server')),
            ],
            options={
                'abstract': False,
                'unique_together': {('name', 'server')},
            },
            bases=('base_resource.basemodel',),
        ),
    ]
