# Generated by Django 4.1.1 on 2022-09-18 15:28

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
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=200)),
                ('prioridade', models.CharField(choices=[('alta', 'alta'), ('media', 'média'), ('baixa', 'baixa')], default='Prioridades', max_length=5)),
                ('status', models.CharField(choices=[('em andamento', 'em andamento'), ('pendente', 'pendente'), ('concluída', 'concluída')], default='---', max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tarefa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
