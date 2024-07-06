from django.db import models
from users.models import User
from shop.models import Products


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    class Meta:
        db_table = 'cart'
        verbose_name = 'Кошик'
        verbose_name_plural = 'кошиків'
    
    objects = CartQueryset().as_manager()
    
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Користувач')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    session_key = models.CharField(max_length=32, blank=True, null=True, verbose_name='Код сеансу')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Кількість')
    created_stamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    
    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
    
    def __str__(self):
        return f"Кошик {self.user.username} | Товар {self.product.product_name} | Кількість {self.quantity}"
