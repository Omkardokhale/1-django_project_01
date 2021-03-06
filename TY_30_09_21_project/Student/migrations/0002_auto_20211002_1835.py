# Generated by Django 3.2.7 on 2021-10-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('RollNo', models.IntegerField(max_length=30)),
                ('Branch', models.CharField(blank=True, max_length=30, null=True)),
                ('CGPA', models.IntegerField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
