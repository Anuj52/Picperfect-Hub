from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Define the URL patterns for the project
urlpatterns = [

    # Include the URL patterns from the 'core' app
    path('', include('core.urls')),
    # Include the URL patterns from the 'item' app
    path('item/', include('item.urls')),
    # Include the URL patterns from the 'dashboard' app
    path('dashboard/', include('dashboard.urls')),
    # Include the Django admin interface URL patterns
     path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Add URL patterns to serve media files during development

# The 'urlpatterns' list contains URL patterns for the project. Each 'path' function call
# defines a URL pattern that maps a URL path to a view function or another URL configuration.
# The 'include' function is used to include URL patterns from other apps, effectively
# allowing a modular approach to organizing URL configurations.

# The first three 'path' calls include the URL patterns defined in the 'urls.py' files
# of the 'core', 'item', and 'dashboard' apps, respectively. For example, when a request
# with a URL path starting with 'item/' is received, it will be forwarded to the 'item.urls'
# URL configuration to further process the URL.

# The fourth 'path' call includes the built-in Django admin interface. When a request
# with a URL path starting with 'admin/' is received, it will be handled by the Django
# admin site, providing an interface to manage the project's data models.

# The '+ static()' part adds URL patterns to serve media files during development.
# The 'static' function is used to serve files from the 'MEDIA_ROOT' directory in response
# to requests with URLs starting with the 'MEDIA_URL'. This is useful for serving user-uploaded
# media files during development.

# Note: This code should be included in the main 'urls.py' file of the Django project,
# typically found at the root level of the project directory. It sets up the URL
# configurations for the entire project, directing requests to the appropriate views
# or apps based on the URL paths.
