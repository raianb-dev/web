from django.db import models

class Event_click(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    email = models.CharField(max_length=255)
    geo_ip = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    history_href = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255)
    button = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    
    class Meta:
         db_table = 'event_click'