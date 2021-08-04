from django.contrib.auth.base_user import BaseUserManager
from cities_light.models import City, Country

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, name, login, country, city, password, **extra_fields):
        values = [email, name, login, country, city]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        country = Country.objects.get(id=country)
        city = City.objects.get(id=city)
        user = self.model(
            email=email,
            name=name,
            login=login,
            #country=country,
            #city=city,
            **extra_fields
        )
        user.country = country
        user.city = city
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, login, country, city, password=None,**extra_fields):
        '''
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        '''
        return self._create_user(email, name, login, country, city, password, **extra_fields)

    def create_superuser(self, email, name, login, country, city, password=None, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        '''
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        '''

        #user.is_admin = True
        #user.save(using=self._db)
        return self._create_user( email, name, login, country, city, password, **extra_fields)