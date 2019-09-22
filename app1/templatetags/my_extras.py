from django import template

register = template.Library()

# invoco decorador para hacer lo mismo de linea 15
@register.filter(name='cut')
def cut(value, arg):
    '''
    Filtro para cortar un argumento 'arg' de un string
    value = variable del contexto diccionario
    '''
    return value.replace(arg, '')

# primer argumento, como se llama en template, segundo funcion
# register.filter('cut', cut)
