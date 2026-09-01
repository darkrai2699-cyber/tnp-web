from django.contrib import admin
from .models import (
    Alumni,
    Admin as AdminModel,
    AlumniCoordinator,
    BatchMentor,
    Batch,
    GraduationYear,
    Event,
    GalleryPhoto,
    Comment,
    Visitor,
    VisitorCount,
)

admin.site.register(Alumni)
admin.site.register(AdminModel)
admin.site.register(AlumniCoordinator)
admin.site.register(BatchMentor)
admin.site.register(Batch)
admin.site.register(GraduationYear)
admin.site.register(Event)
admin.site.register(GalleryPhoto)
admin.site.register(Comment)
admin.site.register(Visitor)
admin.site.register(VisitorCount)
