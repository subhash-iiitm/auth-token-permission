__author__ = 'chowmean'
from models import *



class RolePermission:


    def getUser_id(self,token):
        try:
            dataFields = TokenUsers.objects.get(token=token)
            return dataFields.user_id
        except TokenUsers.DoesNotExist:
            return 0


    def getRole_id(self,token):
        user_id=self.getUser_id(token)
        if user_id==0:
            return 0
        else:
            try:
                dataFields = UserRoles.objects.get(user_id=user_id)
                return dataFields.role_id
            except UserRoles.DoesNotExist:
                return 0


    def getPermission_id(self,permission):
        try:
            dataFields = Permissions.objects.get(name=permission)
            return dataFields.permission_id
        except Permissions.DoesNotExist:
            return 0


    def canAccess(self,token,permission):
        role_id=self.getRole_id(token)
        permission_id=self.getPermission_id(permission)
        try:
            dataFields = PermissionsRoles.objects.get(permission_id=permission_id,role_id=role_id)
            if dataFields.permission_id!=0:
                return True
            else:
                return False
        except PermissionsRoles.DoesNotExist:
            return False

    def isLoggedIn(self,token):
        try:
            dataFields = TokenUsers.objects.get(token=token)
            if dataFields.user_id!=0:
                return True
            else:
                return False
        except TokenUsers.DoesNotExist:
            return False
