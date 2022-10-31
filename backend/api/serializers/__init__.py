try:
	from api.serializers.UserSerializer import UserSerializer

except ImportError:
	from .UserSerializer import UserSerializer
