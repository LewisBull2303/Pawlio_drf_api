from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=100, default='General'),  # Set a default or allow null/blank
            preserve_default=False,
        ),
    ]
