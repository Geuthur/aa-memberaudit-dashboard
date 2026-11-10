# Third Party
from evesde_factory.allianceauth import EveCharacterFactory
from evesde_factory.utils import add_character_to_user
from memberaudit.models import CharacterUpdateStatus
from memberaudit.tests.testdata.factories_2 import CharacterFactory

# Django
from django.http import HttpResponse

# AA Member Audit Dashboard
from madashboard.tests import AuthTestCase
from madashboard.tests.testdata.app import UserMainFactory
from madashboard.views import dashboard_memberaudit_check


class DashboardMemberAuditCheckTest(AuthTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user_without_permission = UserMainFactory(permissions=[])

    def test_dashboard_memberaudit_check_user_with_ma_premission(self):
        # Test Data
        request = self.factory.get("/")
        request.user = self.user
        # Test Action
        response = dashboard_memberaudit_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # Expected Result
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_dashboard_memberaudit_check_user_without_permission(self):
        # Test Data
        request = self.factory.get("/")
        request.user = self.user_without_permission
        # Test Action
        response = dashboard_memberaudit_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # Expected Result
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_dashboard_memberaudit_check_many(self):
        # Test Data
        CharacterFactory(user=self.user)
        CharacterFactory(user=self.user, is_main=False)

        request = self.factory.get("/")
        request.user = self.user
        # Test Action
        response = dashboard_memberaudit_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # Expected Result
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_dashboard_memberaudit_check_character_update_issues(self):
        # Test Data
        # Create a CharacterUpdateStatus with failed update for a character
        memberaudit = CharacterFactory(user=self.user)
        CharacterUpdateStatus.objects.create(
            character=memberaudit, is_success=False, update_finished_at=None
        )

        request = self.factory.get("/")
        request.user = self.user
        # Test Action
        response = dashboard_memberaudit_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # Expected Result
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )
        # Check that the character update issue icon is present
        self.assertIn(
            "<i class='fas fa-triangle-exclamation'",
            response.content.decode("utf-8"),
        )
        # Check that the issue message is present
        self.assertIn(
            "Please re-register this character, as there was an issue with the last update.",
            response.content.decode("utf-8"),
        )

    def test_dashboard_memberaudit_check_character_both_unregistered_and_issues(self):
        # Test Data
        character = CharacterFactory(user=self.user)
        # Add an unregistered character (character without memberaudit record)
        add_character_to_user(user=self.user, character=EveCharacterFactory())
        # Create a CharacterUpdateStatus with failed update for the registered character
        CharacterUpdateStatus.objects.create(
            character=character, is_success=False, update_finished_at=None
        )

        request = self.factory.get("/")
        request.user = self.user
        # Test Action
        response = dashboard_memberaudit_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # Expected Result
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )
        # Check that both icons are present (registration issue and update issue)
        self.assertIn(
            "<i class='fas fa-times-circle'",
            response.content.decode("utf-8"),
        )
        self.assertIn(
            "<i class='fas fa-triangle-exclamation'",
            response.content.decode("utf-8"),
        )
