# Generated by Django 3.2.6 on 2021-12-14 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='nombre de usuario', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(help_text='texto del tweet', max_length=1000)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='aplicacion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDeRetweet', models.DateTimeField(auto_now_add=True)),
                ('tweet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tweet', to='aplicacion.tweet')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarioTweet', to='aplicacion.usuario')),
            ],
        ),
    ]
