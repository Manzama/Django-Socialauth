from socialauth.models import AuthMeta, OpenidProfile, TwitterUserProfile, \
FacebookUserProfile, LinkedInUserProfile, GithubUserProfile, FoursquareUserProfile

from django.contrib import admin

admin.site.register(AuthMeta)
admin.site.register(OpenidProfile)
admin.site.register(TwitterUserProfile)
admin.site.register(FacebookUserProfile)
admin.site.register(LinkedInUserProfile)
admin.site.register(GithubUserProfile)
admin.site.register(FoursquareUserProfile)
