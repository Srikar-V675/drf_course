from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class ContactSerializer(serializers.ModelSerializer):

	name = CharField(source="title", required=True) # pointing to the title field in the model
	message = CharField(source="description", required=True) # pointing to the description field in the model
	email = EmailField(required=True)
	
	class Meta:
		model = models.Contact
		fields = (
			'name',
			'email',
			'message'
		)