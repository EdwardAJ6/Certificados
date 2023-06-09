import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'certificado',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

MYSQLAZURE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd_distribuidora_python',
        'USER': 'admindisoc',
        'PASSWORD': 'Dev1032936760',
        'HOST': 'sqldistribuidora.mysql.database.azure.com',
        'PORT': '3306',
'OPTIONS': {
    'ssl': {'verify_ssl': False},
},
    }
}



