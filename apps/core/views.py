from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib import messages


@require_POST
def toggle_dark_mode(request):
    """Переключение тёмной/светлой темы"""
    if request.session.get('dark_mode'):
        del request.session['dark_mode']
        messages.success(request, 'Светлая тема включена')
    else:
        request.session['dark_mode'] = True
        messages.success(request, 'Тёмная тема включена')

    # Возвращаем туда, откуда пришли
    return redirect(request.META.get('HTTP_REFERER', '/'))


def page_not_found(request, exception):
    """404 ошибка"""
    return render(request, 'core/404.html', {'path': request.path}, status=404)


def server_error(request):
    """500 ошибка"""
    return render(request, 'core/500.html', status=500)


def permission_denied(request, exception):
    """403 ошибка (доступ запрещен)"""
    return render(request, 'core/403.html', status=403)


@requires_csrf_token
def csrf_failure(request, reason=""):
    """403 CSRF ошибка (отдельный шаблон)"""
    return render(request, 'core/403csrf.html', {
        'reason': reason,
        'support_email': getattr(settings, 'SUPPORT_EMAIL', 'heap21@mail.ru'),
    }, status=403)
