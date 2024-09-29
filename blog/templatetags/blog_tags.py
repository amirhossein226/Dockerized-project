from django.template import Library
import urllib
from django.urls import reverse
from django.utils.safestring import mark_safe
register = Library()

farsi_nums = {
    '0': '۰',
    '1': '۱',
    '2': '۲',
    '3': '۳',
    '4': '۴',
    '5': '۵',
    '6': '۶',
    '7': '۷',
    '8': '۸',
    '9': '۹'
}


@register.filter
def to_farsi_num(nums):
    nums = str(nums)
    try:
        for num in nums:
            nums = nums.replace(num, farsi_nums.get(num, num))
        return nums
    except ValueError:
        return nums


@register.filter
def no_space(value):
    return mark_safe(value.replace(' ', '&#8204;'))


@register.simple_tag
def myurl(pa, *args):
    return urllib.parse.unquote(reverse(pa, args=args))


@register.simple_tag
def check(variable, value):
    if variable == value:
        print(f"======================================================{value}")
        return "selected"
    return ''
