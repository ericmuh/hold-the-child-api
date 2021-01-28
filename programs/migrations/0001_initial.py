# Generated by Django 3.1.5 on 2021-01-21 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagementApproach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('goal', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('strategic_plan', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammaticApproach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.program')),
            ],
        ),
        migrations.CreateModel(
            name='MileStone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('cost', models.PositiveIntegerField(blank=True, null=True)),
                ('management_approach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.managementapproach')),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('target', models.CharField(blank=True, max_length=100, null=True)),
                ('cost', models.PositiveIntegerField(blank=True, null=True)),
                ('programmatic_approach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.programmaticapproach')),
            ],
        ),
    ]