# Third Party
import factory
from evesde_factory.allianceauth import EveCharacterFactory, UserFactory
from evesde_factory.utils import add_character_to_user
from memberaudit.models import Character


class UserMainFactory(UserFactory):
    """Generate a User object with a main character and default permissions for Member Audit Dashboard."""

    # The dashboard widget has no own permission, it is shown with Member Audit access.
    permissions__ = ["memberaudit.basic_access"]
    scopes__ = Character.esi_scopes()

    # pylint: disable=no-self-argument
    @factory.post_generation
    def main_character(obj, create, _, **kwargs):
        if not create:
            return
        if "character" in kwargs:
            character = kwargs["character"]
        else:
            character_name = f"{obj.first_name} {obj.last_name}"
            character = EveCharacterFactory(character_name=character_name)

        add_character_to_user(
            user=obj,
            character=character,
            is_main=True,
            scopes=obj._main_character_scopes,
        )
