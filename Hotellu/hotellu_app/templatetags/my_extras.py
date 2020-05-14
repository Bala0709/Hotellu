from django import template

register = template.Library()

@register.filter(name='filtering_val')
def filtering_val(value, arg):
    #Cutting all the value of arg from string
    return value.replace(arg, '')

# register.filter('cut', filtering_val)
