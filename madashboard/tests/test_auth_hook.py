# Django
from django.http import HttpResponse

# AA Member Audit Dashboard
from madashboard.auth_hooks import MemberCheckDashboardHook, register_membercheck_hook
from madashboard.tests import AuthTestCase
from madashboard.tests.testdata.app import UserMainFactory


class TestAuthHooks(AuthTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user_without_permission = UserMainFactory(permissions=[])

    def test_render_returns_empty_string_for_user_without_permission(self):
        # Test Data
        request = self.factory.get("/")
        request.user = self.user_without_permission
        rendered_item = MemberCheckDashboardHook()

        # Test Action
        response = rendered_item.render(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # Expected Result
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_render_returns_widget_for_user_with_permission(self):
        # Test Data
        request = self.factory.get("/")
        request.user = self.user
        rendered_item = MemberCheckDashboardHook()

        # Test Action
        response = rendered_item.render(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # Expected Result
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="memberaudit-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_register_membercheck_hook(self):
        # Test Data
        hooks = register_membercheck_hook()
        # Expected Result
        self.assertIsInstance(hooks, MemberCheckDashboardHook)
