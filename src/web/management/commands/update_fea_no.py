from django.core.management.base import BaseCommand
from web.models import Productfeas
from django.db.models import Count

class Command(BaseCommand):
    help = 'Update feature numbers for existing Productfeas instances'

    def handle(self, *args, **options):
        # Get all products with their feature count
        products = Productfeas.objects.values('product').annotate(feature_count=Count('product'))

        # Iterate through each product and update feature numbers
        for product in products:
            product_id = product['product']
            feature_count = product['feature_count']

            # Update feature numbers for each instance of the product
            features = Productfeas.objects.filter(product_id=product_id)
            for index, feature in enumerate(features, start=1):
                feature.featureno = index
                feature.save()

            self.stdout.write(self.style.SUCCESS(f'Updated feature numbers for Product ID {product_id}, total features: {feature_count}'))