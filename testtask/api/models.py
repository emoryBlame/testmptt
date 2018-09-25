#coding: utf-8

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey 


# Create your models here.
def make_upload_path(instance, filename):
	return (u'api/Group/%s' % filename).encode('utf-8')


class Group(MPTTModel):
	name = models.CharField(max_length = 64, blank = False, verbose_name = 'Название')
	parent = TreeForeignKey('self', null = True, blank = True, on_delete = models.CASCADE, verbose_name = 'Родитель')
	icon = models.ImageField(upload_to = 'api/Group/', blank = False, verbose_name = 'Иконка')
	description =  models.TextField(max_length = 512, blank = True, verbose_name = 'Описание')
	inheritGroup = models.IntegerField(blank = False, default = 0, verbose_name = 'Дочерних Групп')
	inheritElement = models.IntegerField(blank = False, default = 0, verbose_name = 'Дочерних Элементов')

	feilds = ('name', 'parent', 'icon', 'description', 'inheritGroup', 'inheritElement')
	class Meta:
		verbose_name = 'Группа'
		verbose_name_plural = 'Группы'

	class MPTTMeta:
		order_insertion_py = ['name']

	def __str__(self):
		return self.name

	def __init__(self, *args, **kwargs):
		super(Group, self).__init__(*args, **kwargs)	
	
	def save(self, *args, **kwargs):
		qs = Group.objects.all()
		count = 0
		for i in qs:
			if i.parent != None and self.name == i.parent.name:
				count += 1
		self.inheritGroup = count #self.inheritElement = int(Element.objects.filter(parent = self.name).count()) does not work

		qs = Element.objects.all()
		count = 0
		for i in qs:
			if i.parent != None and self.name == i.parent.name:
				count += 1
		self.inheritElement = count
		super(Group, self).save(*args, **kwargs)

		return self
	
	def inheritsList(self):
		groups = Group.objects.filter(parent = self.name)
		elems = Element.objects.filter(parent = self.name)
		return groups, elems


class Element(Group, models.Model):
	date = models.DateField(auto_now_add = True, blank = False, verbose_name = 'Дата')
	checked = models.BooleanField(null = True, verbose_name = 'Заполнен модератором')
	
	feilds = ('date', 'checked')

	class Meta:
		verbose_name = 'Элемент'
		verbose_name_plural = 'Элементы'

	def __init__(self, *args, **kwargs):
		super(Element, self).__init__(*args, **kwargs)

	def save(self, *args, **kwargs):
		super(Element, self).save(*args, **kwargs)