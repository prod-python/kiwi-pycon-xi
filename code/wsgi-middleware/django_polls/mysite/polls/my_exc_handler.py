from django.http import HttpResponse


class ExcHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print("exc handler: Calling next view")
        response = self.get_response(request)
        print("exc handler: back from view")
        return response

    def process_exception(self, request, exception):
        print(f'Got exception: {exception} when processing {request}')
        return HttpResponse("An exception occured!")
