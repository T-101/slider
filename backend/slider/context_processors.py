from slider.models import Settings


def settings_context(request):
    # Now that event gets cached, we can query it on every request!
    return {
        'settings': Settings.load()
    }
