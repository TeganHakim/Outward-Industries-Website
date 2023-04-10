from django.db import models

# Create your models here.
class LearnPost(models.Model):
    type = models.CharField(max_length=100, choices=(('Web Design', 'Web Design'), ('Software', 'Software'), ('Business', 'Business')), blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.CharField(max_length=100)
    author = models.CharField(max_length=100, choices=(('Tegan Hakim', 'Tegan Hakim'), ('Tyler Lumpkin', 'Tyler Lumpkin'), ('Outward Industries', 'Outward Industries')), blank=True, null=True)
    file = models.FileField(upload_to='learn_posts', blank=True, null=True)
    image = models.ImageField(upload_to='learn_posts/images', blank=True, null=True)
    url = models.CharField(max_length=100)
    display = models.BooleanField(default=False)
    def __str__(self):
        return self.title