from .serializers import EmailMessengerSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class EmailMessengerAPI(GenericAPIView) :
    serializer_class = EmailMessengerSerializers

    def post(self, request, *args, **kwargs) :
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message":"email sent successfully",
            "success":True
        })
