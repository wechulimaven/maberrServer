from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
    'username', 
    'postContent', 
    'feedUploaderId',
    'postID' ,
    'userThumbnail' ,
    # postImage ,
    'amount' ,
    'userContacts' ,
    'email' ,
    'postalCode' ,
    'shopUrl' ,
    'address' ,
    'shopLocation' ,
    'shop' ,
    'birthday' ,
    'postTimeStamp' ,
    'postImage' ,
    'postCommentCount',
    'postLikeCount' ,
    'mediaType' ,
    'isPayable'
        )
        model = models.Posts
