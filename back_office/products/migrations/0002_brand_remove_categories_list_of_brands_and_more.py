from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='categories',
            name='list_of_brands',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='list_of_products',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='supplier',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='list_of_brands',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='list_of_categories',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='products_list',
        ),
        migrations.AddField(
            model_name='supplier',
            name='products',
            field=models.ManyToManyField(related_name='suppliers', to='products.product'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brands', models.ManyToManyField(to='products.brand')),
                ('products', models.ManyToManyField(related_name='categories', to='products.product')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='brand',
            name='categories',
            field=models.ManyToManyField(to='products.category'),
        ),
        migrations.AddField(
            model_name='brand',
            name='products',
            field=models.ManyToManyField(related_name='brands', to='products.product'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='brands',
            field=models.ManyToManyField(to='products.brand'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='categories',
            field=models.ManyToManyField(to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
        migrations.DeleteModel(
            name='Brands',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]