# Generated by Django 4.2.2 on 2024-02-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0040_remove_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='domain',
            field=models.CharField(choices=[('Web Development', 'Web Development'), ('AIML', 'AIML'), ('DATA SCIENCE', 'DATA SCIENCE')], max_length=20),
        ),
    ]
