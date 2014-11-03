from django.core import validators
from django.db import models

from oars_auth.models import Department, Student, Professor, DUGC, Course


WAITING = 1
ACCEPTED = 2
REJECTED = 3

REQUEST_STATUS_CHOICES = (
    (WAITING, 'Waiting'),
    (ACCEPTED, 'Accepted'),
    (REJECTED, 'Rejected'),
)


class Request(models.Model):

    course = models.OneToOneField(Course)
    student = models.OneToOneField(Student)
    status = models.PositiveSmallIntegerField(choices=REQUEST_STATUS_CHOICES, default=WAITING)


# class Filter(models.Model):
#
#     course = models.ForeignKey(Course)
#     department = models.ForeignKey(Department, blank=True, null=True)
#     min_semester = models.PositiveSmallIntegerField(
#         validators=[
#             validators.MinValueValidator(1),
#             validators.MaxValueValidator(20),
#         ])
#     max_semester = models.PositiveSmallIntegerField(
#         validators=[
#             validators.MinValueValidator(1),
#             validators.MaxValueValidator(20),
#         ])