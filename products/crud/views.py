from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .forms import ProductForm
from .models import Product
from django.views import generic

# Read Objects
# def home(request):
#     products=Product.objects.all()
#     for product in products:
#         product.remaining=product.total-product.sold
#         product.revenue=product.sold*product.price
#     return render(request,'crud/home.html',{"products":products})
class HomeView(generic.ListView):
    # model=Product
    queryset=Product.objects.all()
    template_name='crud/home.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        for product in queryset:
            product.remaining = product.total - product.sold
            product.revenue = product.sold * product.price
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['page_title'] = 'My Product Dashboard'
        return context
    
#Read Object
class ProductView(generic.DetailView):
    model=Product
    template_name='crud/detail.html'
    context_object_name = 'product'

    def get_object(self):
        object=super().get_object()
        object.remaining = object.total - object.sold
        object.revenue = object.sold * object.price
        return object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'The Product Description'
        return context

#Create Object
# def add(request):
#     if request.method=="POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             name=request.POST.get('name')
#             sold=request.POST.get('sold')
#             total=request.POST.get('total')
#             price=request.POST.get('price')
#             review=request.POST.get('review')
#             product=Product.objects.create(name=name,sold=sold,total=total,price=price,review=review)
#             product.save()
#             return redirect(reverse('crud:home'))
#     else:
#         form = ProductForm()
#     return render(request,'crud/add.html',{'form':form})

class AddView(generic.View):
    def get(self, request):
        form = ProductForm()
        return render(request,'crud/add.html',{'form':form})
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            sold=request.POST.get('sold')
            total=request.POST.get('total')
            price=request.POST.get('price')
            review=request.POST.get('review')
            product=Product.objects.create(name=name,sold=sold,total=total,price=price,review=review)
            product.save()
            return redirect(reverse('crud:home'))
        return render(request,'crud/add.html',{'form':form})


#Delete Object
# def delete(request, id):
#     product=get_object_or_404(Product,pk=id)
#     product.delete()
#     return redirect(reverse('crud:home'))

class DeleteView(generic.View):
    def get(self,request,id):
        product=get_object_or_404(Product,pk=id)
        product.delete()
        return redirect(reverse('crud:home'))


#Update Object
# def update(request,id):
#     product=get_object_or_404(Product,pk=id)
#     if request.method=="POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product.name=request.POST.get('name')
#             product.sold=request.POST.get('sold')
#             product.total=request.POST.get('total')
#             product.price=request.POST.get('price')
#             product.review=request.POST.get('review')
#             product.save()
#             return redirect(reverse('crud:home'))
#     else:
#         form = ProductForm(initial={
#         'name':product.name,
#         'sold':product.sold,
#         'total':product.total,
#         'price':product.price,
#         'review':product.review,
#         })
#     return render(request,'crud/update.html',{'form':form})

class UpdateView(generic.View):
    def get(self,request,id):
        product=get_object_or_404(Product,pk=id)
        form = ProductForm(initial={
        'name':product.name,
        'sold':product.sold,
        'total':product.total,
        'price':product.price,
        'review':product.review,
        })
        return render(request,'crud/update.html',{'form':form})
    
    def post(self,request,id):
        form = ProductForm(request.POST)
        product=get_object_or_404(Product,pk=id)
        if form.is_valid():
            product.name=request.POST.get('name')
            product.sold=request.POST.get('sold')
            product.total=request.POST.get('total')
            product.price=request.POST.get('price')
            product.review=request.POST.get('review')
            product.save()
            return redirect(reverse('crud:home'))
        return render(request,'crud/update.html',{'form':form})