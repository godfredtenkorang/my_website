from django.db import models
from .paystack import PayStack
import secrets

class Payment(models.Model):
    full_name = models.CharField(max_length=300, default="")
    email = models .EmailField(max_length=255, default="")
    phone_number = models.CharField(max_length=20, default=0)
    amount = models.PositiveBigIntegerField()
    ref = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Payments'
        
    def __str__(self) -> str:
        return f"Donation from {self.full_name} - Payment: {self.amount}"
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
        
    def amount_value(self) -> int:
        return self.amount * 100
    
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False