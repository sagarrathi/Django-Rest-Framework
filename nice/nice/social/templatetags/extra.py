from django import template

register=template.Library()

@register.filter(name="extra_cut")
def extra_cut(value,arg):
    """
    This remove all args from string
    """
    value=str(value)
    return value.replace(arg,"")

# register.filter('extra_cut', extra_cut)