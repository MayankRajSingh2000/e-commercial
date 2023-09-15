#We used function there for for html filter
from django import template


register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(data, cart):
    keys = cart.keys()
    for id in keys:
        print(id)
        if int(id) == data.id:
            return True
    return False

#After this, now load in templates

@register.filter(name='cart_quantity')
def cart_quantity(data, cart):
    keys = cart.keys()
    for id in keys:
        print(id)
        if int(id) == data.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(data, cart):
    return data.price * cart_quantity(data, cart)

@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)
    return sum
