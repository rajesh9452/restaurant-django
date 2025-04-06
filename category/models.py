from django.db import models


class Category(models.Model):
    user_id = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    image = models.ImageField(upload_to="categories/images/", blank=True, null=True)

    display_fullwidth = models.BooleanField(default=False)
    hidden_title = models.BooleanField(default=False)
    hidden_image = models.BooleanField(default=False)
    display_link = models.BooleanField(default=False)
    card_show = models.BooleanField(default=True)
    hidden = models.BooleanField(default=False)
    external_link = models.URLField(blank=True, null=True)

    enable_special_category = models.BooleanField(default=False)
    special_category_type = models.CharField(max_length=255, blank=True, null=True)
    display_product_in_separate_category = models.BooleanField(default=False)

    view_format = models.CharField(max_length=50, choices=[('grid', 'Grid'), ('list', 'List')], default='grid')
    promotions = models.ManyToManyField('promotion.Promotion', blank=True)

    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
