from django import template
from datetime import timedelta
from datetime import date
from posts.models import PostEater


register = template.Library()
N = 14

@register.simple_tag
def future(value, format):
    tomorrow = date.today() + timedelta(days=value)
    return tomorrow.strftime(format)

@register.assignment_tag
def future_days():
    day = [0]*N
    for i in range(14):
        day[i] = future(i,"%d %b %Y")
    return day

@register.assignment_tag
def future_persons():
        person = [0]*N
        for i in range(14):
            person[i] = PostEater.objects.filter(submit_time__date=future(i,"%Y-%m-%d"))
        return person

@register.assignment_tag
def future_weekdays():
        weekday = [0]*N
        for i in range(14):
            weekday[i] = future(i,"%A")
        return weekday
