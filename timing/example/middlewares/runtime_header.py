from time import time


class RunTimeHeaderMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        # time the view
        start = time()
        response = view_func(request, *view_args, **view_kwargs)
        total_time = time() - start

        response['X-Runtime'] = total_time
        return response