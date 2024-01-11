# Generated by Django 3.2.5 on 2023-12-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishingdate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boat',
            old_name='url_boat_photo',
            new_name='URLBoat',
        ),
        migrations.RenameField(
            model_name='boat',
            old_name='boat_license_type',
            new_name='boatLicenseType',
        ),
        migrations.RenameField(
            model_name='excursion',
            old_name='title',
            new_name='excursionTitle',
        ),
        migrations.RenameField(
            model_name='excursion',
            old_name='excursion_yype',
            new_name='excursionType',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='url',
            new_name='URLFish',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='url',
            new_name='URLAvatar',
        ),
        migrations.RemoveField(
            model_name='boat',
            name='fabrication_year',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='id_booker',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='id_excursion',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='nb_booked_seats',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='excursion',
            name='date_time_list',
        ),
        migrations.RemoveField(
            model_name='excursion',
            name='excursion_price',
        ),
        migrations.RemoveField(
            model_name='excursion',
            name='id_boat',
        ),
        migrations.RemoveField(
            model_name='excursion',
            name='id_owner',
        ),
        migrations.RemoveField(
            model_name='excursion',
            name='number_of_passengers',
        ),
        migrations.AddField(
            model_name='boat',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='idBooker',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='idExcursion',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='nbBookedSeats',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='totalPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='excursion',
            name='dateTimeList',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='excursion',
            name='excursionPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='excursion',
            name='idBoat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='excursion',
            name='idOwner',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='excursion',
            name='numberOfPassengers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='boat',
            name='bedsNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='boat',
            name='capacity',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='boat',
            name='deposit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='boat',
            name='equipments',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='boat',
            name='horsepower',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='boat',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='boat',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='comment',
            field=models.CharField(max_length=1023),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='released',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='size',
            field=models.DecimalField(decimal_places=1, max_digits=1),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='activity',
            field=models.CharField(max_length=1023),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='languages',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='siretNumber',
            field=models.IntegerField(null=True),
        ),
    ]
