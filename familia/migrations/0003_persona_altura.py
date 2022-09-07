from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0002_persona_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='altura',
            field=models.FloatField(default=0.0),
        ),
    ]
