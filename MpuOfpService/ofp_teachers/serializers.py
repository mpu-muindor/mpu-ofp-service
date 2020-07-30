from rest_framework import serializers
from .models import *
import GeneralPhysicalTraining

class AttendanceListSerializer(serializers.ModelSerializer):

    gym = serializers.SlugRelatedField(slug_field = "name", read_only = True)

    class Meta:
        model = Attendance
        fields = ("student", "group", "attendance_date", "gym")


#class AddAttendanceSerializer(serializers.Serializer):
#
#    selected_student = serializers.CharField(max_length = 150)
#    selected_group = serializers.CharField(max_length = 7)
#    selected_attendance_date = serializers.DateField()
#    GYMS = (
#        (1, "№1")
#        )
#    selected_gym = serializers.ChoiceField(choices = GYMS)
#
#    def save(self, **kwargs):
#
#        
#
#        Attendance.objects.create(
#            student=self.validated_data["selected_student"],
#            group=self.validated_data["selected_group"],
#            attendance_date=self.validated_data["selected_attendance_date"],
#            gym=self.validated_data["selected_gym"],
#            )

class AddAttendanceSerializer(serializers.ModelSerializer):

    #student = serializers.CharField(max_length = 150)
    #group = serializers.CharField(max_length = 7)
    #attendance_date = serializers.DateField()
    #gym = serializers.RelatedField(GeneralPhysicalTraining.models.Gymnasium, on_delete=models.CASCADE, null=True)

    class Meta:
        model = Attendance
        fields = "__all__"