# Generated by Django 2.0.3 on 2018-11-17 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=255)),
                ('turn_count', models.IntegerField()),
                ('selected_word_id_1', models.IntegerField()),
                ('selected_word_id_2', models.IntegerField()),
                ('point', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Game')),
            ],
        ),
    ]
