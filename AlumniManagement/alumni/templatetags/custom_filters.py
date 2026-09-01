from django import template

register = template.Library()


@register.filter
def split_chunks(value, chunk_size):
    chunk_size = int(chunk_size)
    return [value[i:i + chunk_size] for i in range(0, len(value), chunk_size)]
