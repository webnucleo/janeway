__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"

from django.conf.urls import url
from core.homepage_elements.about import views

urlpatterns = [
    # Featured Articles
    url(r'^$', views.journal_description, name='journal_description'),
]
