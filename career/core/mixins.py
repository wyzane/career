from io import BytesIO
import xlsxwriter
from django.http.response import JsonResponse


class ResponseMixin:

    code_message = {
        "00000": "成功",
        "00001": "参数错误,",
        "00002": "对象不存在",
        "00003": "对象已存在",
        "00004": "创建错误，",
        "00005": "登录失败",
        "00006": "请重新登录",
        "00007": "es错误"
    }

    def __init__(self):
        self._code = "00000"
        self._status = True
        self._message = "成功"

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, msg):
        self._message = msg
        # self._message = (self.code_message
        #                  .get(self.code) + msg)

    def get_json_response(self, data=None, **kwargs):
        res = dict()
        res["code"] = self.code
        res["status"] = self.status
        res["message"] = self.message
        res = {**res, **kwargs}
        res["data"] = data
        return JsonResponse(res)

    def get_xlsx_response(self, filename, data):
        """下载数据为xlsx格式

        Args:
            filename: 文件名称
            data: 待下载数据
        """
        resp = HttpResponse()
        resp["Content-Type"] = "application/octet-stream"
        resp["Content-Disposition"] = ("attachment;filename={0}.xlsx"
                                       .format(filename))
        resp.write(data)
        return resp

    def download_xlsx(self, headers, data, sheet):
        """返回待下载xlsx数据

        Args:
            headers: 表头
            data: 待下载数据，格式[{...}, {...}, {...}]
            sheet: sheet名称

        Returns:
            output.getValue(): 返回给前端的响应数据

        """
        output = BytesIO()
        wb = xlswriter.WorkBook(output)
        wb_sheet = wb.add_sheet(sheet)

        header_col = 0
        row_num = 0
        for header in headers:
            wb_sheet.write(0, header_col, header)
            header_col += 1

        for d in data:
            for row_col in range(len(headers)):
                wb_sheet.write(row_num, row_col,
                               d.get(headers[row_col]))
            row_num += 1

        wb.close()
        return output.getValue()
