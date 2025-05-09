# Generated by Django 5.2 on 2025-05-07 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("User", "0002_rename_name_user_name_and_more"),
        ("property", "0004_rename_image_property_image_cover_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Offers",
            fields=[
                ("offer_id", models.AutoField(primary_key=True, serialize=False)),
                ("offer_price", models.FloatField()),
                ("expire_date", models.DateTimeField()),
                (
                    "buyer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="User.user"
                    ),
                ),
                (
                    "property_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="property.property",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="offerdata.status",
                    ),
                ),
            ],
        ),
    ]
