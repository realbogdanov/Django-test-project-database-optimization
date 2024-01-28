from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
	context_object_name = "articles"
	queryset = (
		Article.objects
		.select_related("author", "category")
		.prefetch_related("tags")
		.defer("content")
	)
