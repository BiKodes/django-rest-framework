from rest_framework.decorators import api_view
from rest_framework.throttling import UserRateThrottle

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def hello_world(request):

    if request.method == 'POST':
        return Response({"message": "Got some data!": request.data})
    return Response({"message": "Jambo, dunia!"})


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'


@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def view(request):
    return Response({"message": "Jambo leo, tuonane kesho!"})