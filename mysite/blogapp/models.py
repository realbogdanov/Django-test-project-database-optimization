from django.db import models


class Author(models.Model):
	"""Модель, которая представляет автора статьи"""
	name = models.CharField(max_length=100, db_index=True)
	bio = models.TextField()


class Category(models.Model):
	""""Модель, которая представляет категорию статьи"""
	name = models.CharField(max_length=40, db_index=True)


class Tag(models.Model):
	""""Модель, которая представляет тег, который можно назначить статье"""
	name = models.CharField(max_length=40, db_index=True)


class Article(models.Model):
	"""Модель, которая представляет статью"""
	title = models.CharField(max_length=200)
	content = models.TextField()
	pub_date = models.DateTimeField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE, db_index=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, db_index=True)
	tags = models.ManyToManyField(Tag)
