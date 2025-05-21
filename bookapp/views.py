from django.shortcuts import render,get_list_or_404,redirect
from .models import Book
from .forms import BookForm

# Create your views here.


def book_list(request):
    books =Book.objects.all()
    return render(request,'bookapp/book_list.html',{'books':books})

def book_create(request):
    if request.method == 'POST' :
        form =BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'bookapp/book_form.html',{'form':form})

def book_update(request,pk):
    book = get_list_or_404(Book,pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(isinstance=book)
    return render(request,'bookapp/book_form.html',{"form":form})


def book_delete(request,pk):
    book = get_list_or_404(Book,pk=pk)
    if request.method=="POST":
        book.delete()
        return redirect('book_list')
    
    return render(request,'bookapp/book_confirm_delete.html',{"book":book})
