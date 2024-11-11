from django.db import models

# Define your model here
class List(models.Model):
    # Define priority levels
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
    
    # Fields
    id = models.AutoField(primary_key=True)  
    task = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    due_date = models.DateField()  
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default=MEDIUM,  # Default priority
    )

    def __str__(self):
        return self.task
