# Generated by Django 4.0.2 on 2022-02-21 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=10000)),
                ('limit', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hotel_type', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('no_of_days_advance', models.IntegerField()),
                ('start_date', models.DateField()),
                ('hotel_image', models.ImageField(default='0.jpeg', upload_to='media')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='user_auth.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_image', models.ImageField(upload_to='media')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='media')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventImages', to='booking.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotelEvent', to='booking.hotel'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('amount', models.FloatField()),
                ('booked_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventName', to='booking.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to='user_auth.customuser')),
            ],
        ),
    ]