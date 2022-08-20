from django.contrib import admin
from .models import Docs, Talk, Build

admin.site.register(Docs)
admin.site.register(Talk)
admin.site.register(Build)
