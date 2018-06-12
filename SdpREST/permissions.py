from SdpREST.settings.base import PERMISSIONS
from sdp.models.userLevel import UserLevel


class Permission:
    @staticmethod
    def verify(request, allowed):
        if not PERMISSIONS:
            return True

        level_title = UserLevel.objects.which_level(request.LEVEL_ID)

        return level_title in allowed
