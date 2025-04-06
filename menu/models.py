from django.db import models

class Menu(models.Model):
    class MenuType(models.TextChoices):
        GRID_WITH_IMAGES = 'GRID_WITH_IMAGES', 'Grid with images'
        GRID_WITH_TEXT = 'GRID_WITH_TEXT', 'Grid with Text'

    license = models.ForeignKey('accounts.License', on_delete=models.CASCADE)  # Link to License
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=100, blank=True, null=True)
    cover_image = models.ImageField(upload_to='menu/covers/', null=True, blank=True)
    logo_image = models.ImageField(upload_to='menu/logos/', null=True, blank=True)
    category_image = models.ImageField(upload_to='menu/categories/', null=True, blank=True)
    category_background_image = models.ImageField(upload_to='menu/categories/', null=True, blank=True)
    product_image = models.ImageField(upload_to='menu/products/', null=True, blank=True)
    loading_image = models.ImageField(upload_to='menu/loading/', null=True, blank=True)
    app_icon_image = models.ImageField(upload_to='menu/aap_icon/', null=True, blank=True)
    chef_recommends_image = models.ImageField(upload_to='menu/recommends/', null=True, blank=True)
    desktop_image = models.ImageField(upload_to='menu/desktop/', null=True, blank=True)

    # Additional Settings True/ False
    discount_percentage = models.BooleanField(default=False)
    skip_onboarding_screen = models.BooleanField(default=False)
    display_properties_product = models.BooleanField(default=False)
    display_categories_in_home_screen = models.BooleanField(default=False)
    menu_type = models.CharField(
        max_length=20,
        choices=MenuType.choices,
        default=MenuType.GRID_WITH_IMAGES
    )
    display_product_variation_prices = models.BooleanField(default=False)

    # Additional Text
    header_text = models.TextField(blank=True, null=True)
    footer_text = models.TextField(blank=True, null=True)
    product_footer_text = models.TextField(blank=True, null=True)
    cart_footer_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
