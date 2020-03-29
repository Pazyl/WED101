from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.category_name
        }

    def __str__(self):
        return '{}: {}'.format(self.id, self.category_name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField(default='')
    count = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_info': {
                'category_id': self.category_id.id,
                'category_name': self.category_id.category_name
            }
        }

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


