from sdp.tests.TestSuite import TestSuit


class UserTests(TestSuit):
    def test_to_string_method(self):
        self.assertEquals(str(self.admin_user), 'admin')

    def test_is_admin_method(self):
        self.assertEquals(self.admin_user.is_admin, True)
        self.assertEquals(self.admin_user.is_normal, False)
        self.assertEquals(self.admin_user.is_viewer, False)

    #def test_is_normal_method(self):
    #    self.assertEquals(self.normal_user.is_admin, False)
    #    self.assertEquals(self.normal_user.is_normal, True)
    #    self.assertEquals(self.normal_user.is_viewer, False)

    #def test_is_viewer_method(self):
    #    self.assertEquals(self.view_user.is_admin, False)
    #    self.assertEquals(self.view_user.is_normal, False)
    #    self.assertEquals(self.view_user.is_viewer, True)