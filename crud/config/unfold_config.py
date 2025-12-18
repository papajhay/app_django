from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "SPORT STORE Admin",
    "SITE_HEADER": _("Administration SPORT STORE"),
    "SITE_SUBHEADER": _("Gestion des produits"),
    "SHOW_ACTIONS": True, 
    "SITE_URL": "/",
    "SHOW_LANGUAGES": True,
    "TOPBAR": True,
    "LANGUAGES": {
        "navigation": [
            {
                'bidi': False,
                'code': 'fr',
                'name': _("French"),
                'name_local': "Français",
                'name_translated': _("French"),
            },
            {
                'bidi': False,
                'code': 'en',
                'name': _("English"),
                'name_local': "English",
                'name_translated': _("English"),
            },
            {
                'bidi': False,
                'code': 'de',
                'name': _("German"),
                'name_local': "Deutsch",
                'name_translated': _("German"),
            },
        ],
    },
    "CUSTOM_CSS": [
        "unfold/css/styles.css",  
    ],
    "SITE_SYMBOL": "speed",
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("images/logo.jpg"),
        },
    ],
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_BACK_BUTTON": False,
    "BORDER_RADIUS": "5px",
    "COLORS": {
        "base": {
            "50": "oklch(98.5% .002 247.839)",
            "100": "oklch(96.7% .003 264.542)",
            "200": "oklch(92.8% .006 264.531)",
            "300": "oklch(87.2% .01 258.338)",
            "400": "oklch(70.7% .022 261.325)",
            "500": "oklch(55.1% .027 264.364)",
            "600": "oklch(44.6% .03 256.802)",
            "700": "oklch(37.3% .034 259.733)",
            "800": "oklch(27.8% .033 256.848)",
            "900": "oklch(21% .034 264.665)",
            "950": "oklch(13% .028 261.692)",
        },
        "primary": {
            "50": "oklch(97.7% .014 308.299)",
            "100": "oklch(94.6% .033 307.174)",
            "200": "oklch(90.2% .063 306.703)",
            "300": "oklch(82.7% .119 306.383)",
            "400": "oklch(71.4% .203 305.504)",
            "500": "oklch(62.7% .265 303.9)",
            "600": "oklch(55.8% .288 302.321)",
            "700": "oklch(49.6% .265 301.924)",
            "800": "oklch(43.8% .218 303.724)",
            "900": "oklch(38.1% .176 304.987)",
            "950": "oklch(29.1% .149 302.717)",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "command_search": False,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Navigation"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Tableau de bord"),
                        "icon": "home",
                        "link": reverse_lazy("admin:index"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Utilisateurs"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": _("Produits"),
                        "icon": "production_quantity_limits",
                        "link": reverse_lazy("admin:products_product_changelist"),
                    },
                ],
            },
        ],
    },
}

#from django.templatetags.static import static
#from django.urls import reverse_lazy
#from django.utils.translation import gettext_lazy as _

#UNFOLD = {
#    "SITE_TITLE": "SPORT STORE Admin",
#    "SITE_HEADER": "Administration SPORT STORE",
#    "SITE_SUBHEADER": "Gestion des produits",

#    "SITE_URL": "/",
#    "SHOW_ACTIONS": True,
#    "SHOW_LANGUAGES": True,
#    "TOPBAR": True,

#    "LANGUAGES": {
#        "navigation": [
#            {"code": "fr", "name": _("French"), "name_local": "Français"},
#            {"code": "en", "name": _("English"), "name_local": "English"},
#            {"code": "de", "name": _("German"), "name_local": "Deutsch"},
#        ],
#    },

#    "CUSTOM_CSS": [
#        "unfold/css/styles.css",
#    ],

#    "SIDEBAR": {
#        "show_search": True,
#        "navigation": [
#            {
#                "title": _("Navigation"),
#                "items": [
#                    {
#                        "title": _("Dashboard"),
#                        "icon": "home",
#                        "link": reverse_lazy("admin:index"),
#                    },
#                    {
#                        "title": _("Produits"),
#                        "icon": "inventory",
#                        "link": reverse_lazy("admin:products_product_changelist"),
#                    },
#                ],
#            },
#        ],
#    },
#}
