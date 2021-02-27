from django.db import models

# Create your models here.
class Posts(models.Model):
    username = models.CharField(blank=True, max_length=50)
    postContent = models.CharField(blank=True,max_length=50)
    feedUploaderId = models.CharField(blank=True,max_length=50)
    postID = models.CharField(blank=True,max_length=50)
    userThumbnail = models.CharField(blank=True,max_length=50)
    postImage = models.CharField(blank=True,max_length=50)
    amount = models.CharField(blank=True,max_length=50)
    userContacts = models.CharField(blank=True,max_length=50)
    email = models.CharField(blank=True,max_length=50)
    postalCode = models.CharField(blank=True,max_length=50)
    shopUrl = models.CharField(blank=True,max_length=50)
    address = models.CharField(blank=True,max_length=50)
    shopLocation = models.CharField(blank=True,max_length=50)
    shop = models.CharField(blank=True,max_length=50)
    birthday = models.CharField(blank=True,max_length=50)

    postTimeStamp = models.DateTimeField(blank=True,)
    # postImage = models.FileField(blank=True,)
    postCommentCount = models.IntegerField(blank=True,)
    postLikeCount = models.IntegerField(blank=True,)
    mediaType = models.BooleanField(default=False)
    isPayable = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username},{self.postContent},{self.postTimeStamp}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'