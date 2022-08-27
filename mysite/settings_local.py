import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'greenverse',
        'USER': 'greenverse',
        'PASSWORD': '',
        'HOST': 'greenverse.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}


