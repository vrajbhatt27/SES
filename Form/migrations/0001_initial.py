# Generated by Django 3.2.6 on 2021-09-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField(null=True)),
                ('event_name', models.CharField(max_length=50, null=True)),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Form.user')),
            ],
        ),
    ]
