from django.db import models

class Sprint(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "Sprint %s" % self.name

class Story(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return "Story %s" % self.name

class DOD(models.Model):
    story = models.OneToOneField(
        Story,
        on_delete=models.CASCADE,
        primary_key = True)
    test_coverage_done = models.BooleanField(default = False)
    integration_test_done = models.BooleanField(default = False)

    def __str__(self):              # __unicode__ on Python 2
        return "Dod for %s" % self.story.name
