from django.http import HttpResponse  
from TestModel.models import Test


def database(request):  
    # 删除id=1的数据  
    test = Test.objects.get(id=1)  
    test.delete()  
    # 另外一种方式  
    # Test.objects.filter(id=1).delete()  
    # 删除所有数据  
    # Test.objects.all().delete()  
    return HttpResponse("<p>数据删除成功</p>")