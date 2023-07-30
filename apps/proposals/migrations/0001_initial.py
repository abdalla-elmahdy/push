# Generated by Django 4.2.3 on 2023-07-30 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motive', models.TextField(max_length=350)),
                ('skillset', models.TextField(max_length=350)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact_details', models.TextField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals_received', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='projects.project')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals_sent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]