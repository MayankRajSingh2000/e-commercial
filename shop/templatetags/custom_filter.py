#We used function there for for html filter
#Filter for currency
from django import template


register = template.Library()
# first search rupyee symbole and paste there
@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)

# now we load this custom filter where we want to use this

# for orders.html
@register.filter(name='multiply')
def multiply(number, number1):
    return number * number1
