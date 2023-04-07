# Generated by Django 4.1.7 on 2023-03-16 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c1', models.SmallIntegerField()),
                ('c2', models.SmallIntegerField()),
                ('c3', models.SmallIntegerField()),
                ('c4', models.SmallIntegerField()),
                ('c5', models.SmallIntegerField()),
                ('c6', models.SmallIntegerField()),
                ('account', models.CharField(max_length=100)),
                ('dp', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=2)),
                ('amount', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_account', to='app.account')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_transaction', to='app.transaction')),
            ],
        ),
    ]
