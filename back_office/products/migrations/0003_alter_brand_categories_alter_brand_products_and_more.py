from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_brand_remove_categories_list_of_brands_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="categories",
            field=models.ManyToManyField(blank=True, to="products.category"),
        ),
        migrations.AlterField(
            model_name="brand",
            name="products",
            field=models.ManyToManyField(
                blank=True, related_name="brands", to="products.product"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="brands",
            field=models.ManyToManyField(blank=True, to="products.brand"),
        ),
        migrations.AlterField(
            model_name="category",
            name="products",
            field=models.ManyToManyField(
                blank=True, related_name="categories", to="products.product"
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="brands",
            field=models.ManyToManyField(blank=True, to="products.brand"),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="categories",
            field=models.ManyToManyField(blank=True, to="products.category"),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="products",
            field=models.ManyToManyField(
                blank=True, related_name="suppliers", to="products.product"
            ),
        ),
    ]