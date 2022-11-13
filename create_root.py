from django.contrib.auth import get_user_model

# see ref. below
UserModel = get_user_model()

if not UserModel.objects.filter(username='root').exists():
    user = UserModel.objects.create_user('root', password='root')
    user.is_superuser=True
    user.is_staff=True
    user.save()

