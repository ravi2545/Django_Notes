filter_value  = request.GET.get("filter", None)
        year_value = request.GET.get("year", None)
        # result = some_func(filter_value, year_value)
        k = sample(filter_value, year_value)
        result = k.year_filtering()
        return HttpResponse("PLEASE ENTER CORRECT  DATE IN URL DATA")

        # if request.GET.get("filter", None)=='category':
        #     year(s=f)

class sample():
    def __init__(self, filter, year):
        self.filter = filter

    def year_filtering(self):
