from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            'id',
            'name',
            'alias',
            'cover_image',
            'logo_image',
            'category_image',
            'category_background_image',
            'product_image',
            'loading_image',
            'app_icon_image',
            'chef_recommends_image',
            'desktop_image',
            'discount_percentage',
            'skip_onboarding_screen',
            'display_properties_product',
            'display_categories_in_home_screen',
            'menu_type',
            'display_product_variation_prices',
            'header_text',
            'footer_text',
            'product_footer_text',
            'cart_footer_text',
            'license'
        ]

    def to_internal_value(self, data):
        # Ensure 'discount_percentage', 'skip_onboarding_screen', etc. are properly converted to booleans
        if 'discount_percentage' in data:
            data['discount_percentage'] = data['discount_percentage'] in ['true', 'True', '1', 'on']
        if 'skip_onboarding_screen' in data:
            data['skip_onboarding_screen'] = data['skip_onboarding_screen'] in ['true', 'True', '1', 'on']
        if 'display_properties_product' in data:
            data['display_properties_product'] = data['display_properties_product'] in ['true', 'True', '1', 'on']
        if 'display_categories_in_home_screen' in data:
            data['display_categories_in_home_screen'] = data['display_categories_in_home_screen'] in ['true', 'True',
                                                                                                      '1', 'on']
        return super().to_internal_value(data)