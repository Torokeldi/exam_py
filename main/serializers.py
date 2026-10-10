from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Курстун аталышы бош болбошу керек."
            )
        return value.strip()

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Баасы терс сан болбошу керек."
            )
        return value

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Узактыгы нөлдөн чоң болушу керек."
            )
        return value