

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacultyView', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='s_name',
        ),
        migrations.AddField(
            model_name='student',
            name='s_fname',
            field=models.CharField(default=5, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='s_lname',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
