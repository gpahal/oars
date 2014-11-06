import re

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


class RestrictAccessMiddleware(object):
    """
    Middleware component that wraps the login_required decorator around
    matching URL patterns. Restricts access for Students, Professors, DUGC's
    and other users.
    """
    def __init__(self):
        self.student = re.compile(settings.STUDENT_ACCESS_URL)
        self.professor = re.compile(settings.PROFESSOR_ACCESS_URL)
        self.dugc = re.compile(settings.DUGC_ACCESS_URL)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # No need to process URLs if user already logged in
        is_student = self.student.match(request.path)
        is_professor = self.professor.match(request.path)
        is_dugc = self.dugc.match(request.path)

        restriction_needed = is_student or is_professor or is_dugc

        if restriction_needed and not request.user.is_authenticated():
            return login_required(view_func)(request, *view_args, **view_kwargs)

        # An exception match should immediately return None
        if self.student.match(request.path):
            if not hasattr(request.user, 'student'):
                raise PermissionDenied
            return None

        elif self.professor.match(request.path):
            if not hasattr(request.user, 'professor'):
                raise PermissionDenied
            return None

        elif self.dugc.match(request.path):
            if not hasattr(request.user, 'dugc'):
                raise PermissionDenied
            return None

        else:
            return None