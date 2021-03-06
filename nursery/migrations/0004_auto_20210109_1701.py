# Generated by Django 3.1.5 on 2021-01-09 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0003_auto_20210109_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='nursery.order')),
                ('plant', models.ManyToManyField(to='nursery.Plant')),
            ],
        ),
        migrations.DeleteModel(
            name='OrderPlantProperty',
        ),
    ]
