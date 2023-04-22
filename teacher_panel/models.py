from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.
class Teacher(models.Model):
    SCHOOL_TYPE = [
        ("junior", "junior"),
        ("senior", "senior"),
    ]
    school_level = models.CharField(max_length=6, choices=SCHOOL_TYPE, default="junior")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher")
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    zone = models.ForeignKey("general.Zone", on_delete=models.CASCADE, null=True)
    district = models.ForeignKey("general.District", on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='profile')
    school = models.ForeignKey("general.School", on_delete=models.CASCADE)
    remove = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} => {self.school.name}"
    
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_user")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="student")
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(upload_to='profile')
    date_of_birth = models.DateField(null=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} => {self.teacher.school.name}"
    
    def save(self, *args, **kwargs):
        if not self.user:
            # Generate username and password
            username = slugify(self.full_name) + get_random_string(5)
            password = get_random_string(8)

            # Create user account
            user = User.objects.create_user(username=username, password=password)
            user.email = self.email
            user.save()
            self.user = user

            # Send login details to student's email
            # subject = 'Your login details for the competition platform'
            # message = render_to_string('login_details_email.html', {'username': username, 'password': password})
            # send_mail(subject, message, 'admin@competition-platform.com', [self.email], fail_silently=False)

        super(Student, self).save(*args, **kwargs)
