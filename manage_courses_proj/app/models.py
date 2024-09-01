from django.db import models

class Course(models.Model):
    course_code = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=50)
    credits = models.PositiveSmallIntegerField()

    def __str__(self):
        txt = "{0}, ({1})"
        return txt.format(self.name, self.credits)