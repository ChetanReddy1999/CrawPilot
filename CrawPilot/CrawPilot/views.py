from django.http import JsonResponse
from Utils import scrap
import json, threading
from uuid import uuid4

def scrap_urls(request):
    urls = json.loads(request.body)['urls']

    rand_id = str(uuid4().hex)
    
    background_thread = threading.Thread(name=rand_id,target=scrap.get_data,daemon=True,args=(urls,rand_id))
    background_thread.start()

    return JsonResponse({'message':'Scarp for the urls has been started..!!','id':rand_id})

def give_result(request):
    id = json.loads(request.body)['id']

    response_str = "Crawling is completed!!"
    for thread in threading.enumerate():
        if thread.name == id:
            response_str = "Crawling is still in progress!!"
            break
    
    if response_str == "Crawling is completed!!":
        response_str = scrap.ans[id]

    return JsonResponse({'result':response_str})


def report_urls(request):
    ans = scrap.return_urls()
    return JsonResponse({'result':ans})


def vector_embed(request):
    id = json.loads(request.body)['id']
    cosine = scrap.vector_embeddings(id)

    return JsonResponse({'result':cosine})



