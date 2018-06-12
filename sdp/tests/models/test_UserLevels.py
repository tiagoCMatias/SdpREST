from sdp.models.userLevel import UserLevel
from sdp.tests.TestSuite import TestSuit


class LevelTests(TestSuit):
    def test_which_level_queryset(self):
        queryset = UserLevel.objects.which_level(10000)
        self.assertEqual(queryset.count(), 0)
        queryset = UserLevel.objects.which_level(1)
        self.assertEquals(queryset.count(), 1)
        self.assertEquals(queryset.get().title, 'Admin')

    def test_admin_level_queryset(self):
        queryset = UserLevel.objects.admin_level().get()
        self.assertEquals(queryset.id, 1)

    def test_normal_level_queryset(self):
        queryset = UserLevel.objects.normal_level().get()
        self.assertEquals(queryset.id, 2)

    def test_view_level_queryset(self):
        queryset = UserLevel.objects.viewer_level().get()
        self.assertEquals(queryset.id, 3)

