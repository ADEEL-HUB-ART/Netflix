from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to a user
    otp = models.CharField(max_length=6)  # 6-digit OTP
    is_verified = models.BooleanField(default=False)  # OTP verification status
    created_at = models.DateTimeField(auto_now_add=True)  # OTP generation time

    def is_valid(self):
        """Check if the OTP is still valid (5 min expiration)."""
        return datetime.now() < self.expires_at

    def __str__(self):
        return f"OTP for {self.user.username}: {self.otp}"
