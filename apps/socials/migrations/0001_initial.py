# Generated by Django 4.0.6 on 2022-08-03 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qr_image', models.ImageField(blank=True, null=True, upload_to='qrcodes')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('social_media_name', models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('linkedin', 'Linkedin'), ('instagram', 'Instagram'), ('github', 'Github'), ('reddit', 'Reddit'), ('quora', 'Quora'), ('instagram', 'Instagram'), ('others', 'Others')], max_length=150)),
                ('url', models.URLField(default='https://')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texts',
                'ordering': ('-created_on',),
            },
        ),
    ]