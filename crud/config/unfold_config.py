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
