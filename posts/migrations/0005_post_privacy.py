

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20191229_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='privacy',
            field=models.BooleanField(default=True),
        ),
    ]
