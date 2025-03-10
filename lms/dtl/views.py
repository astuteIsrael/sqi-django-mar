from django.shortcuts import render

# Create your views here.
def dtl_syntax(request):
    context = {

        'user': 'Israel',
        'cart': ['tomato', 'strawberry', 'vanilla ice cream', 'burger', 'cake'],
        'is_favorite': True,
        'no_of_items': 5
    }
    return render(request, 'dtl/dtl.html', context)
