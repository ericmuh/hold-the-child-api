# Generated by Django 3.1.5 on 2021-01-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('document_type', models.CharField(blank=True, choices=[('Ethics', 'Ethics'), ('Standards', 'Standards'), ('Policies', 'Policies'), ('Memos', 'Memos'), ('Manual', 'Manual')], max_length=100, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('name_of_publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]