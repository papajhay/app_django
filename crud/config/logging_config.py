import logging.config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# ===== FORMAT PERSONNALISÉ =====
LOG_FORMAT = "%(asctime)s | %(levelname)s | [%(filename)s:%(lineno)d] | %(message)s"

LOGGING = {
    "version": 1,
    # Les loggers Django par défaut sont d’abord désactivés
    # Ensuite seuls ceux que tu définis dans "loggers" seront actifs
    "disable_existing_loggers": True,

    # ---------- FORMATTERS ----------
    # Les formatters définissent comment le texte du log sera affiché.
    "formatters": {
        "default": {
            "format": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },

    # ---------- HANDLERS ----------
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",          # ← on passe à INFO (plus de DEBUG SQL)
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "app.log",
            "maxBytes": 10 * 1024 * 1024, # Si le fichier dépasse 10 Mo, il est renommé en app.log.1, et un nouveau fichier app.log est créé.
            "backupCount": 10, # Maximum 10 fichiers archivés (app.log.1 → app.log.10).
            "formatter": "default",
            "level": "INFO",
            "encoding": "utf-8", # Permet d’écrire correctement les caractères accentués dans le fichier.
        },
        # MAGIE : ce handler n'écrit RIEN dans la console
        #  -------------- Pour bloquer : -----------------
        # les requêtes SQL (django.db.backends)
        # les logs du serveur (django.server)
        # les logs du reloader (django.utils.autoreload)
        "null": {
            "class": "logging.NullHandler",
        },
    },

    "loggers": {
         "app.products": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": False,
        },
        # Logger utilisé par Django pour les requêtes SQL
        "django.db.backends": {
            "handlers": ["null"],
            "level": "DEBUG",
            "propagate": False,
        },
        # Logger utilisé par le reloader Django (runserver)
        "django.utils.autoreload": {      
            "level": "INFO",
            "propagate": False,
        },
        # Logger utilisé par le serveur Django (runserver)
        # C’est lui qui écrit les requêtes HTTP :
        "django.server": {
            "handlers": ["null"],  # bloque totalement les logs HTTP
            "level": "INFO",
            "propagate": False,
        },
        # Logger général pour Django
        # Envoie vers : file (donc app.log)
        # Niveau minimal : WARNING 
        "django": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}

logging.config.dictConfig(LOGGING)
