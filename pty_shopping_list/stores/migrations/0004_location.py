# Generated by Django 3.2.11 on 2022-01-25 23:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_remove_storechain_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('store_chain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations', to='stores.storechain', verbose_name='Store chain')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
