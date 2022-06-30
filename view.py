from django.http import HttpResponse
def index(request):
    return HttpResponse("""<button><a href="/about">About</a></button>
    <button><a href="/capfirst">capital</a></button>""")

def about(request):
    return HttpResponse("""<button><a href="/">Back</a></button>
                        <h1>hello omkar</h1>""")
def capfirst(request):
    return HttpResponse("""<button><a href="/">Back to home page</a><button> 
    <h1>capitalized words</h1>""")
