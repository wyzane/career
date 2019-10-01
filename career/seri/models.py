"""嵌套序列化测试model
"""

from django.contrib.postgres.fields import JSONField
from django.db import models

from core.models import DateTimeModel


class Student(DateTimeModel,
              models.Model):

    DISPLAY_FIELDS = ("id", "name", "grade", "course")

    id = models.AutoField(
        primary_key=True,
        verbose_name="学生编号",
        help_text="学生编号")
    name = models.CharField(
        max_length=32,
        default="小明",
        null=False,
        verbose_name="学生姓名",
        help_text="学生姓名")
    grade = models.IntegerField(
        default=1,
        verbose_name="年级",
        help_text="学生年级")
    course = JSONField(
        verbose_name="课程信息",
        help_text="课程信息")

    class Meta:
        db_table = "seri_student"
        verbose_name = "学生表"


class Course(DateTimeModel,
             models.Model):
    course_id = models.AutoField(
                primary_key=True,
                verbose_name="课程编号",
                help_text="课程编号")
    course_name = models.CharField(
        max_length=32,
        default="python",
        null=False,
        verbose_name="课程名称",
        help_text="课程名称")
    teacher = JSONField(
        verbose_name="老师信息",
        help_text="老师信息")

    class Meta:
        db_table = "seri_course"
        verbose_name = "课程表"


class Teacher(DateTimeModel,
              models.Model):

    TEACHER_CHOICE = (
        (1, "common"),
        (2, "header"),
        (3, "director"),
    )

    code = models.AutoField(
           primary_key=True,
           verbose_name="教师编号",
           help_text="教师编号")
    name = models.CharField(
           max_length=32,
           default="Tony",
           null=False,
           verbose_name="教师名称",
           help_text="教师名称")
    position = models.IntegerField(
        choices=TEACHER_CHOICE,
        verbose_name="教师职位",
        help_text="教师信息")

    class Meta:
        db_table = "seri_teacher"
        verbose_name = "教师表"
