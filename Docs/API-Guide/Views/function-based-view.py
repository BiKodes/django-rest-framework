from rest_framework.decorators import api_view
from rest_framework.throttling import UserRateThrottle
from rest_framework.schemas import AutoSchema

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


class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):



@api_view(['GET'])
@schema(CustomAutoSchema())
def view(request):
    return Response({"ujumbe": "Habari za Mombasani! Kwema!"})

@api_view(['GET'])
@schema(None)
def view(request):
    return Response({"Ujumbe": "Leo ilikumufti!"})