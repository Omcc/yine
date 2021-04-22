from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
# Create your models here.

class Subject(MPTTModel):
    name = models.CharField(max_length=50,unique=True)
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True, related_name='children')
    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = _("Subject")
        verbose_name_plural = _('Subjects')

    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('Subject'))
    title = models.ImageField(upload_to='questions')
    option1 = models.ImageField(upload_to='questions', verbose_name=_('Option 1'))
    option2 = models.ImageField(upload_to='questions', verbose_name=_('Option 2'))
    option3 = models.ImageField(upload_to='questions', verbose_name=_('Option 3'))
    option4 = models.ImageField(upload_to='questions', verbose_name=_('Option 4'))

    class Meta:
        verbose_name=_('Question')
        verbose_name_plural = _('Questions')