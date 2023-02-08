from django import template

register = template.Library()

def count(obj) -> int:
    return obj.count()

def day(obj):
    dict = {0: 'السبت', 1: 'الأحد', 2: 'الاثنين', 3: 'الثلاثاء', 4: 'الأربعاء', 5: 'الخميس'}
    return dict[obj]

def get_state(obj):
    dict = {0: 'صالح', 1: 'يحتاج للصيانة', 2: 'تالف'}
    return dict[obj]

register.filter('count', count)
register.filter('day', day)
register.filter('get_state', get_state)