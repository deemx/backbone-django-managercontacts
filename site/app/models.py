from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField( max_length=50 )
    last_name = models.CharField( max_length=50 )
    email_address = models.EmailField( unique=True )
    description = models.TextField( null=True )
    
    def __str__(self):
        return '{0} {1}: {2}'.format(self.first_name,
                                     self.last_name,
                                     self.email_address)
