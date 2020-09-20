# users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
     
     joined_date = serializers.ReadOnlyField()
     
     class Meta(object):
          model = User
          fields = ('id','email','first_name','last_name','joined_date','password')
          extra_kwargs = {'password':{'write_only':True}} 
 