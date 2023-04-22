# Generated by Django 4.2 on 2023-04-20 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_panel', '0007_student_teacher_remove_teacher_profile_district_and_more'),
        ('general', '0004_alter_school_administrator'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Local_Government',
            new_name='Zone',
        ),
        migrations.RenameField(
            model_name='competition',
            old_name='can_join_with_link',
            new_name='send_result_immediately',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='local_government',
            new_name='zone',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='local_government',
            new_name='zone',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='joining_password',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='number_of_allowed_attempt',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='request_password_when_using_link',
        ),
        migrations.RemoveField(
            model_name='school',
            name='administrator',
        ),
        migrations.RemoveField(
            model_name='school',
            name='type_of_school',
        ),
        migrations.AddField(
            model_name='competition',
            name='allowed_school_type',
            field=models.CharField(choices=[('all', 'all'), ('junior', 'junior'), ('senior', 'senior')], default='all', max_length=7),
        ),
        migrations.AddField(
            model_name='competition',
            name='maximum_number_of_students',
            field=models.IntegerField(default=2, help_text='enter maximum number of student a school can register.'),
        ),
        migrations.AddField(
            model_name='competition',
            name='show_result_immediately',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='competition',
            name='show_score_immediately',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='competition',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='school_level',
            field=models.CharField(choices=[('junior', 'junior'), ('senior', 'senior')], default='junior', max_length=6),
        ),
        migrations.AlterField(
            model_name='competition',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='ending_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='exam_duration',
            field=models.DurationField(help_text='total amount of time the exam should be taken place.'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='exam_status',
            field=models.CharField(choices=[('not started', 'not started'), ('started', 'started'), ('ended', 'ended')], default='not started', help_text="don't edit this until you know what you are doing.", max_length=11),
        ),
        migrations.AlterField(
            model_name='competition',
            name='starting_at',
            field=models.DateTimeField(null=True),
        ),
    ]
