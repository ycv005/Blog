from django.shortcuts import render

# Create your views here. Views play the important logic, it will take request from the model
#pass it to the template(blog/post_list.html)

def post_list(request):
    return render(request,'blog/post_list.html',{})