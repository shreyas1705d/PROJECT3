from django.db import models

class Customer(models.Model):
    PRODUCT_CHOICES = [
        ('product1', 'Product 1'),
        ('product2', 'Product 2'),
        ('product3', 'Product 3'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    product = models.CharField(max_length=100, choices=PRODUCT_CHOICES, default='product1')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service_quality = models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])
    product_quality = models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])
    delivery_speed = models.IntegerField(choices=[(1, 'Slow'), (2, 'Average'), (3, 'Fast')])
    overall_experience = models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])
    additional_comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback from {self.name} ({self.email})'

