from django import template

register = template.Library()

@register.filter(name='stime')
def secondTime(value):
    mins, sec = divmod(value, 60)
    heure , mins = divmod(mins, 60)
    return "%02d:%02d:%02d" % (heure,mins, sec)
    

#register.filter(name='stime', secondTime)