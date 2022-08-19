import time


def latency_reporter(get_response):
    print(f"Initializaing {__name__}")

    def middleware(request):
        request_begin = time.time()
        response = get_response(request)
        print(f"Request{request} took {time.time()-request_begin} seconds")
        return response

    return middleware
