from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    company = models.TextField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name


class Posts(models.Model):
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
