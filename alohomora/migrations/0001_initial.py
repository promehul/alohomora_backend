# Generated by Django 2.2.3 on 2020-05-19 15:21

import alohomora.models.question
import alohomora.models.user_profile
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=alohomora.models.question.Question.user_directory_path)),
                ('question_text', models.TextField(blank=True, max_length=1000)),
                ('answer', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_image', models.ImageField(default='default_profile_image.png', upload_to=alohomora.models.user_profile.UserProfile.user_directory_path)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('question_on', models.IntegerField(default=1)),
            ],
        ),
    ]
