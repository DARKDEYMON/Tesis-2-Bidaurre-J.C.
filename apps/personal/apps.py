from django.apps import AppConfig
from django.apps import apps

#User = apps.get_model('auth', 'User')

class PersonalConfig(AppConfig):
	name = 'personal'
def create_perms():
	from django.contrib.auth.models import User
	from django.contrib.auth.models import Permission
	from django.contrib.contenttypes.models import ContentType
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_personal',
			name='Ver personal',
			content_type=content_type,
		)
	except:
		print ("permiso 1 ya aderido")
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_seguimiento',
			name='Ver seguimineto',
			content_type=content_type,
		)
	except:
		print ("permiso 2 ya aderido")
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_almacen',
			name='Ver almacen',
			content_type=content_type,
		)
	except:
		print ("permiso 3 ya aderido")
#create_perms()