# Generated by Django 3.0 on 2020-01-21 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=140)),
                ('last_name', models.CharField(max_length=140)),
                ('born', models.DateField()),
                ('died', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('-year', 'title')},
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Person')),
            ],
            options={
                'unique_together': {('movie', 'person', 'name')},
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='acting_credits', through='core.Role', to='core.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='directed', to='core.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='writers',
            field=models.ManyToManyField(blank=True, related_name='writing_credits', to='core.Person'),
        ),
    ]
