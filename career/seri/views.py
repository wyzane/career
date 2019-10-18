"""drf nest serializer
"""

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from core.mixins import ResponseMixin
from public.decorators import TraceMemory
from settings.startup import run
from .models import Student
from .serializer import StudentSerializer

# 服务器启动时初始化
run()


class StudentList(ResponseMixin, APIView):
    """查询信息
    """

    parser_classes = [JSONParser]

    @TraceMemory(top=5)
    def post(self, request):

        args = request.data
        if args:
            student_id = args.get("studentId")
            if student_id:
                student = (Student.objects
                           .filter(id=student_id).first())

                serializer = StudentSerializer(instance=student)
                data = serializer.data
                return self.get_json_response(data)
        self.code = "00001"
        self.status = False
        self.message = "参数错误"
        return self.get_json_response()


class StudentCreation(ResponseMixin, APIView):
    """创建Student
    """

    parser_classes = [JSONParser]

    def post(self, request):
        args = request.data
        if args:
            serializer = StudentSerializer()
            student_obj = serializer.create(args)
            data = {
                "student_id": student_obj.id
            }
            return self.get_json_response(data)
        self.code = "00001"
        self.status = False
        self.message = "参数错误"
        return self.get_json_response()
