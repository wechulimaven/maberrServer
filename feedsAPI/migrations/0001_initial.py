# Generated by Django 2.2.18 on 2021-02-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50)),
                ('postContent', models.CharField(blank=True, max_length=50)),
                ('feedUploaderId', models.CharField(blank=True, max_length=50)),
                ('postID', models.CharField(blank=True, max_length=50)),
                ('userThumbnail', models.CharField(blank=True, max_length=50)),
                ('amount', models.CharField(blank=True, max_length=50)),
                ('userContacts', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('postalCode', models.CharField(blank=True, max_length=50)),
                ('shopUrl', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('shopLocation', models.CharField(blank=True, max_length=50)),
                ('shop', models.CharField(blank=True, max_length=50)),
                ('birthday', models.CharField(blank=True, max_length=50)),
                ('postTimeStamp', models.DateTimeField(blank=True)),
                ('postImage', models.FileField(blank=True, upload_to='')),
                ('postCommentCount', models.IntegerField(blank=True)),
                ('postLikeCount', models.IntegerField(blank=True)),
                ('mediaType', models.BooleanField(default=False)),
                ('isPayable', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Posts',
                'verbose_name_plural': 'Posts',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
