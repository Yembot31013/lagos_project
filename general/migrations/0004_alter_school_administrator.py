# Generated by Django 4.1.7 on 2023-02-26 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_panel', '0002_teacher_profile_district_and_more'),
        ('general', '0003_alter_school_administrator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='administrator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='school_admintrator', to='teacher_panel.teacher_profile'),
        ),
    ]
