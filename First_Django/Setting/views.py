from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Setting


class SettingView(APIView):
    def get(self, request, format=None):
        try:
            settings_dict = {
                setting.name: setting.value for setting in Setting.objects.all()
            }
            return Response(settings_dict, status=200)
        except:
            return Response({"Bad Request"}, status=400)

    def post(self, request, format=None):
        try:
            settings = request.data.get('settings', [])
            bad_settings = []

            for setting in settings:
                try:
                    Setting.objects.update_or_create(
                        name=setting['NAME'],
                        defaults={'value': setting['VALUE']}
                    )
                except Exception as e:
                    bad_settings.append({"setting": setting, "error": str(e)})

            if bad_settings:
                return Response({"INVALID SETTINGS": bad_settings}, status=400)
            return Response({"message": "Settings saved successfully"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
