from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify

# Create your models here.
class Competition(models.Model):
    STATUS_CHOICES = [
        ('not started', 'not started'),
        ('started', 'started'),
        ('ended', 'ended'),
    ]
    SCHOOL_TYPE = [
        ("all", "all"),
        ("junior", "junior"),
        ("senior", "senior"),
    ]
    name = models.CharField(max_length=80, help_text="enter the name of the competition which will display physically.")
    description = models.TextField(help_text="give brief explanation of the competition.")
    exam_status = models.CharField(max_length=11, choices=STATUS_CHOICES, default="not started", help_text="don't edit this until you know what you are doing.")
    exam_duration = models.DurationField(help_text="total amount of time the exam should be taken place.")
    allowed_school_type = models.CharField(max_length=7, choices=SCHOOL_TYPE, default="all")
    custom_link_slug = models.CharField(max_length=100)
    show_score_immediately = models.BooleanField(default=False)
    show_result_immediately = models.BooleanField(default=False)
    send_result_immediately = models.BooleanField(default=False)
    maximum_number_of_students = models.IntegerField(default=2, help_text="enter maximum number of student a school can register.")
    starting_at = models.DateTimeField(null=True)
    ending_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.custom_link_slug:
            slug_text = slugify(self.name)
            while Competition.objects.filter(custom_link_slug = slug_text):
                new_slug_text = self.name + " " + get_random_string(5)
                slug_text = slugify(new_slug_text)
            self.custom_link_slug = slug_text
        
        super(Competition, self).save(*args, **kwargs) # Call the real save() method


class District(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Zone(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, related_name='zone', on_delete=models.CASCADE, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.district.name} => {self.name}"
    
class School(models.Model):
    SCHOOL_LEVEL = [
        ("junior", "junior"),
        ("senior", "senior"),
    ]
    name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_level = models.CharField(max_length=6, choices=SCHOOL_LEVEL, default="junior")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.zone.name} => {self.district.name} => {self.name} => {self.school_level}"


    

