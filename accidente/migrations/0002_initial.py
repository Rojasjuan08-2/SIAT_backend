import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accidente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='accidente',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aprobaciones',
            name='accidente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aprobaciones', to='accidente.accidente'),
        ),
        migrations.AddField(
            model_name='aprobaciones',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='aprobaciones',
            unique_together={('usuario', 'accidente')},
        ),
    ]
