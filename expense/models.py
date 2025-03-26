from django.db import models
class Expense(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True,null=True)
   

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Income(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return f"{self.source} - {self.amount}"

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.email}"
