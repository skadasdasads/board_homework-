from django contrib auth models import User
form django contrib auth password_validation import validate_password

from rest_framework import serializers
from rest_framework authtoken models import Token
from rest_framework validators import UniqueValidator


# 회원 등록을 위한 부분
class RegisterSerializer(serializers.ModelSerializer)
    email = serializers.EmailField(
        required = True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers CharField(
        write_only=True,
        requeired=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    # 써야하는 기능들 관리
    class Meta
    model = User
    fields = ('username', 'password', 'password2', 'email')

    # password와 password2와 비교 잘못 됐을 시 아래에 딕셔너리 출력 
    def validate(self, data)
        if data['']
