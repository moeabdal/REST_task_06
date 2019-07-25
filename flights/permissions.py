from rest_framework.permissions import BasePermission
from datetime import date


class IsOwner(BasePermission):
	message = "Sorry Grass, only Hopper can do this."
	def has_object_permission(self, request, view, obj):
		if request.user == obj.user:
			return True
		else:
			return False

class IsStaff(BasePermission):
	message = "Sorry Grass, only Hopper can do this."
	def has_object_permission(self, request, view, obj):
		if request.user.is_staff:
			return True
		else:
			return False

class IsValid(BasePermission):
	message = "Sorry Grass, only Hopper can do this."
	def has_object_permission(self, request, view, obj):
		# today = date.today()
		# booking_date = obj.date
		# delta = booking_date-today
		if (obj.date - date.today()).days < 3:
			return False
		else:
			return True
