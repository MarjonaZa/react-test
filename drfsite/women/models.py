from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user=models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE())

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True) #выяснить что такое db_inedx
# это удобный способ указать Django автоматически оптимизировать запросы к определённым полям через индексацию.
    def __str__(self):
        return self.name

