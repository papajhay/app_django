SPECTACULAR_SETTINGS = {
    'TITLE': 'SPORT STORE API',
    'DESCRIPTION': "Documentation de l'API pour la gestion des produits du SPORT STORE",
    'VERSION': '1.0.0',
    
    # Swagger UI config
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'docExpansion': 'none',
    },

    # Favicon ou logo dans Swagger UI
    'SWAGGER_UI_FAVICON_HREF': '/static/images/logo.jpg',

    # Pour forcer l'utilisation des fichiers locaux de Swagger UI
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_BUNDLE_JS': 'drf_spectacular_sidecar/swagger-ui-bundle.js',
    'SWAGGER_UI_STANDALONE_PRESET_JS': 'drf_spectacular_sidecar/swagger-ui-standalone-preset.js',
    'SWAGGER_UI_CSS': 'drf_spectacular_sidecar/swagger-ui.css',
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}
