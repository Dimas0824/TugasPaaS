import logging

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

logger = logging.getLogger("core")


def home(request):
    access_time = timezone.localtime()
    logger.info(
        "HOME_ACCESS path=%s method=%s app_name=%s",
        request.path,
        request.method,
        settings.APP_NAME,
    )

    context = {
        "app_name": settings.APP_NAME,
        "status": "OK",
        "access_time": access_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "environment": settings.DJANGO_ENV,
    }
    return render(request, "core/home.html", context)


def health(request):
    logger.info(
        "HEALTH_ACCESS path=%s method=%s app_name=%s",
        request.path,
        request.method,
        settings.APP_NAME,
    )
    return JsonResponse(
        {
            "status": "ok",
            "app_name": settings.APP_NAME,
            "environment": settings.DJANGO_ENV,
        }
    )
