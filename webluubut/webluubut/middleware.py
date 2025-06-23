from django.core.exceptions import RequestDataTooBig, TooManyFieldsSent
from django.contrib import messages
from django.shortcuts import redirect

class UploadLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except RequestDataTooBig:
            messages.error(request, "Dung lượng dữ liệu vượt quá giới hạn cho phép.")
            return redirect(request.path)
        except TooManyFieldsSent:
            messages.error(request, "Số lượng trường trong form vượt quá giới hạn.")
            return redirect(request.path)