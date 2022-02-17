# Generated by Django 3.2.11 on 2022-02-03 11:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("authnapp", "0003_alter_shopuser_activation_key_expires")]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 5, 11, 21, 20, 862385, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        )
    ]
