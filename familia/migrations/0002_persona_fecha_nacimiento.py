from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
