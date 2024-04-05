import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta'  # Clave secreta para proteger formularios
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'  # URI de la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilita el seguimiento de modificaciones en SQLAlchemy

    # Configuración de correo electrónico (por ejemplo, para restablecimiento de contraseña)
    # MAIL_SERVER = 'smtp.example.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
