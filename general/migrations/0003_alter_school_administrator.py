# Generated by Django 4.1.7 on 2023-02-26 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_panel', '0002_teacher_profile_district_and_more'),
        ('general', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='administrator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='school_admintrator', to='teacher_panel.teacher_profile'),
        ),
    ]
