from myblog.models import Article,Category

def get_result():
    sorted_list=[]
    get_none_list=Category.objects.filter(p_category=None).all()
    sorted_list=get_sorted_category(get_none_list)
    return sorted_list
def get_sorted_category(get_none_list):
    sorted_list=[]
    for i in get_none_list:
        sorted_list.append(i)
        if i.childs.exists():
            sorted_list.extend(get_sorted_category(i.childs.all()))
    return sorted_list