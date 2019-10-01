"""嵌套序列化创建model对象和获取model对象
序列化作用：1. 校验数据，创建model对象
            2. 序列化model数据，返回给前端
"""

from rest_framework import serializers

from .models import Student, Course, Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ("code", "name", "position")

    def create(self, validated_data):
        """create
        """
        instacne = Teacher.objects.create(**validated_data)
        return instacne

    def update(self, instance, validated_data):
        pass


class CourseSerializer(serializers.ModelSerializer):

    teacher = TeacherSerializer()

    class Meta:
        model = Course
        fields = ("course_id", "course_name", "teacher")

    def create(self, validated_data):
        """create
        """
        instacne = Course.objects.create(**validated_data)
        teacher = validated_data.get("teacher")
        if teacher:
            instacne_teacher = TeacherSerializer()
            instacne_teacher.create(teacher)
        return instacne

    def update(self, instance, validated_data):
        pass


class StudentSerializer(serializers.ModelSerializer):

    course = CourseSerializer()

    class Meta:
        model = Student
        fields = ("id", "name", "grade", "course")

    def create(self, validated_data):
        """create
        """
        instacne = Student.objects.create(**validated_data)

        course = validated_data.get("course")
        if course:
            instacne_course = CourseSerializer()
            instacne_course.create(course)
        return instacne

    def update(self, instance, validated_data):
        pass
