from rest_framework import viewsets
from .models import parent
from .serializers import ParentSerializer
import cv2
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ParentViewSet(viewsets.ModelViewSet):
    queryset = parent.objects.all()
    serializer_class = ParentSerializer


class ParentPhotoUpload(APIView):
    def post(self, request, pk):
        obj = get_object_or_404(parent, pk=pk)

        uploaded = request.FILES.get("photo")
        if not uploaded:
            return Response({"error": "No photo uploaded"}, status=400)

        # Save the uploaded image
        obj.photo = uploaded
        obj.save()

        # 👉 OPTIONAL: face detection example
        image_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
        img = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                             "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(img, 1.3, 5)

        if len(faces) == 0:
            return Response({"error": "No face detected"}, status=400)

        return Response({
            "message": "Photo uploaded and face detected",
            "faces_detected": len(faces)
        })
   



