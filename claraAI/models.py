from django.db import models
import uuid

class SessionLog(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    request_data = models.TextField()
    response_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.session_id)