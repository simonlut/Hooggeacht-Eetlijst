from django import template
from datetime import timedelta
from datetime import date
from posts.models import PostEater


register = template.Library()
N = 14

@register.simple_tag
def future(value, format):
    tomorrow = date.today() + timedelta(days=value+1)
    return tomorrow.strftime(format)

@register.assignment_tag
def future_days():
    day = [0]*N
    for i in range(N):
        day[i] = future(i,"%d %b %Y")
    return day

@register.assignment_tag
def keys():
    key = [0]*N
    for i in range(N):
        day[i] = i
    return key

@register.simple_tag
def future_persons():
        persons = [0]*N
        for i in range(N):
            persons[i] = PostEater.objects.filter(submit_time__date=future(i,"%Y-%m-%d"))
        if len(persons)>0:
            return list(persons)
        else:
            return "f"

@register.assignment_tag
def future_weekdays():
        weekday = [0]*N
        for i in range(N):
            weekday[i] = future(i,"%A")
        return weekday

@register.inclusion_tag("../templates/posts/posteater_template.html")
def posts_future():
        things = PostEater.objects.all()
        return {'things':things}
