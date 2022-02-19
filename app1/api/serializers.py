from rest_framework.serializers import *
from ..models import User
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterSer(ModelSerializer):
    password=CharField(write_only=True,error_messages={'required':'password key is required','blank':'password  is required'})
    email=CharField(error_messages={'required':'email key is required','blank':'email is required'})
    username=CharField(error_messages={'required':'username key is required','blank':'username is required'})
    class Meta:
        model = User
        fields=('email','username','gender','first_name','profile_image','id_proof','mobile','password')


class SignupSer(Serializer):
    password=CharField(write_only=True,error_messages={'required':'password key is required','blank':'password  is required'})
    email=CharField(error_messages={'required':'email key is required','blank':'email is required'})
    username=CharField(error_messages={'required':'username key is required','blank':'username is required'})
    
    def validate(self,data):
        username=data.get('username')
        qs=User.objects.filter(username=data.get('username'))
        if qs.exists():
            raise ValidationError("Username already exists")
        
        qs=User.objects.filter(email=data.get('email'))
        if qs.exists():
            raise ValidationError("Email already exists")
        return data

    def create(self,validated_data):
        obj=User.objects.create(username=validated_data.get('username'),email=validated_data.get('email'))
        obj.set_password(validated_data.get('password'))
        obj.save()
        return validated_data


class LoginSer(Serializer):
    email=EmailField(error_messages={'required':'Email key is required','blank':'Email is required'})
    password=CharField(error_messages={'required':'Password key is required','blank':'Password is required'})
    token=CharField(read_only=True, required=False)

    def validate(self,data):
        qs=User.objects.filter(email=data.get('email'))
        if not qs.exists():
            raise ValidationError('No account with this email')
        user=qs.first()
        if user.check_password(data.get('password'))==False:
            raise ValidationError('Invalid Password')
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        data['token']='JWT'+str(token)
        return data


'''class UpdateSer(ModelSerializer):
    class Meta:
        model = User
        fields=('email','username','gender','first_name')'''


class UpdateSer1(Serializer):
    email=EmailField(error_messages={'required':"enter a valid email",'blank':'Enter a  email'})
    username=CharField(error_messages={'required':"enter a valid username",'blank':'Enter a  username'})
    def update(self,instance,validated_data):
        instance.email=validated_data.get('email')
        instance.username=validated_data.get('username')
        instance.save()
        return validated_data

class DeleteSer(ModelSerializer):
    class Meta:
        model = User
        fields=('__all__')


