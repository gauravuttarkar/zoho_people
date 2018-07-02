# Generated by Django 2.0.6 on 2018-06-25 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIntegration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yellowant_user_id', models.IntegerField()),
                ('yellowant_team_subdomain', models.CharField(max_length=256)),
                ('yellowant_integration_id', models.IntegerField(unique=True)),
                ('yellowant_integration_invoke_name', models.CharField(max_length=256)),
                ('yellowant_integration_token', models.CharField(max_length=2048)),
                ('auth_token', models.CharField(max_length=2048, null=True)),
                ('update_login_flag', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='YellowAntRedirectState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=512)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]