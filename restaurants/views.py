from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list" : [
    {"restaurant_name":"Hurdees", "food_type" : "Fast"},
    {"restaurant_name":"Burkin", "food_type" : "Dry"},
    {"restaurant_name":"McDont", "food_type" : "Poison"}
    ]

    }
    return  render(request, 'list.html', context)


def restaurant_detail(request):

    context = { "my_object" : {"restaurant_name":"Hurdees", "food_type":"Fast"} 

    }
    return render(request, 'detail.html', context)
