from .models import Institution


#TODO: run as daily task?
def populate_article_count():
    for obj in Institution.objects.all():
        obj.spacescoop_count = len(obj.scoops.all())
        obj.save()
