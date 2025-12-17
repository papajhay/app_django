from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
import warnings
from rest_framework import serializers

# Supprimer l’avertissement inutile de BeautifulSoup (liés aux URLs)
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


class CleanHTMLMixin:
    """
    Mixin pour nettoyer le HTML à l'entrée (sauvegarde) et à la sortie (affichage).
    """

    def clean_html(self, value):
        """
        Nettoie une chaîne HTML pour renvoyer du texte brut.
        """
        if not value or not isinstance(value, str):
            return value

        soup = BeautifulSoup(value, "html.parser")

        # Supprimer les balises indésirables
        for tag in soup(["script", "style", "div"]):
            tag.decompose()

        # Supprimer tous les attributs HTML (class, style, id, etc.)
        for tag in soup.find_all(True):
            tag.attrs = {}

        # Retourner le texte brut
        return soup.get_text(separator=" ", strip=True)

    def to_representation(self, instance):
        """
        Nettoie tous les champs texte lors de la sortie (GET).
        """
        ret = super().to_representation(instance)
        for field_name, value in ret.items():
            if isinstance(value, str):
                ret[field_name] = self.clean_html(value)
            elif isinstance(value, list):
                ret[field_name] = [
                    self.clean_html(item) if isinstance(item, str) else item
                    for item in value
                ]
            elif isinstance(value, dict):
                ret[field_name] = {
                    k: self.clean_html(v) if isinstance(v, str) else v
                    for k, v in value.items()
                }
        return ret

    def to_internal_value(self, data):
        """
        Nettoie les champs texte lors de l'entrée (POST, PUT, PATCH).
        """
        if isinstance(data, dict):
            cleaned_data = {}
            for key, value in data.items():
                cleaned_data[key] = (
                    self.clean_html(value) if isinstance(value, str) else value
                )
            data = cleaned_data
        return super().to_internal_value(data)
