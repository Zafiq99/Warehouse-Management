from WInventory.models import InventoryItem, Category, InboundItem, OutboundItem
import csv


def run():
    with open('scripts/inventory_data.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        InventoryItem.objects.all().delete()
        Category.objects.all().delete()
        InboundItem.objects.all().delete()
        OutboundItem.objects.all().delete()

        for row in reader:
            print(row)

            category, _ = Category.objects.get_or_create(name=row[1])
            items = InventoryItem(name=row[0],
                        category=category,
                        sku=row[2],
                        quantity=row[3],
                        location=row[4],
                        supplier=row[5]
                        )
            items.save()