from .models import VisitorCount


class VisitorCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('visited'):
            request.session['visited'] = True
            visitor, _ = VisitorCount.objects.get_or_create(id=1)
            visitor.count += 1
            visitor.save()
        response = self.get_response(request)
        return response
