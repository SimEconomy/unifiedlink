from django.db import models

class CRMEntity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ...  # Other fields depending on the architecture
