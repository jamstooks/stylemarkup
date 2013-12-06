from django.db import models

# def get_upload_path(instance, filename):
#     return instance.get_upload_path(instance, filename)
# 
# class Theme(models.Model):
#     name = models.CharField(max_length=16)
#     slug = models.SlugField(max_length=16)
#     author = models.CharField(max_length=64)
#     
# class ThemeVersions(models.Model):
#     theme = models.ForeignKey(Theme)
#     version = models.CharField(max_length=8)
#     css_file = models.FileField(upload_to=get_upload_path)
#     
#     def get_upload_path(self, instance, filename):
#         return "themes/%s/%s/" % (instance.theme.slug, instance.version)
