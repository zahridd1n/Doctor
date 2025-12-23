from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    price = models.CharField(max_length=255)
    student_price = models.CharField(max_length=255)
    image = models.ImageField(upload_to="courses",null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    text2 = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class CoursePhotos(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE,         related_name="photos")
    image = models.ImageField(upload_to="course_photos")

    def __str__(self):
        return self.course.title

    class Meta:
        verbose_name = "course photo"
        verbose_name_plural = "course photos"


class CourseRegister(models.Model):
    JOB_CHOICES = (
        ('student', 'СТУДЕНТ'),
        ('teacher', 'ВРАЧ'),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    job = models.CharField(
        max_length=20,
        choices=JOB_CHOICES
    )
    message = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "course register"
        verbose_name_plural = "course registers"