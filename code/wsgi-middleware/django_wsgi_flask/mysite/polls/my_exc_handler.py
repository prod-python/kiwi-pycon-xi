from django.http import HttpResponse


class ExecHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print(f'Got exception: {exception} when processing {request}')
        return HttpResponse("An exception occured!")
