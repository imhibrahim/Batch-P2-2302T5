from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import productform
from django.core.files.storage import FileSystemStorage
import os,uuid
from .models import product_collection
from bson import ObjectId


def fatchproduct(request):
      product=list(product_collection.find())
     
      for p in product:
          p['id']=str(p["_id"]) #Create New Column 
          del p['_id']
      return render(request,'product.html',{"data":product})

def Insertproduct(request):
    if request.method=="POST":
        form=productform(request.POST,request.FILES)
        if form.is_valid():
            image_url= None
            if 'pic' in request.FILES:
                image=request.FILES['pic']
                ext=os.path.splitext(image.name)[1]
                new_name=f"{uuid.uuid4()}{ext}"
                fs=FileSystemStorage()
                filname=fs.save(new_name,image)
                image_url=fs.url(filname)
            data={
                'name': form.cleaned_data['name'],
                'price': form.cleaned_data['price'],
                'desc': form.cleaned_data['Description'],
                'pic': image_url
            }
            product_collection.insert_one(data)
            return redirect('index')
    else:
        form=productform()
        return render(request,'pinsert.html',{'productform':form})


def delproduct(request,id):
    product_collection.delete_one({"_id":ObjectId(id)})
    return redirect('index')

def edit(request,id):
    product=product_collection.find_one({"_id":ObjectId(id)})
    if request.method=="POST":
        form=productform(request.POST,request.FILES)
        if form.is_valid():
            data={
                'name':form.cleaned_data['name'],
                'price':form.cleaned_data['price'],
                'desc':form.cleaned_data['Description']
            }
            if 'pic' in request.FILES:
                image=request.FILES['pic']
                ext=os.path.splitext(image.name)[1]
                new_name=f"{uuid.uuid4()}{ext}"
                fs=FileSystemStorage()
                filname=fs.save(new_name,image)
                image_url=fs.url(filname)
                data['pic']=image_url
            product_collection.update_one(
                {"_id":ObjectId(id)},
                {"$set":data }
            )
            return redirect('index')
    else:
        form=productform(initial={
            'name':product['name'],
            'price':product['price'],
            'Description':product['desc'],
        })
        return render(request,'editproduct.html',{'data':form})
    
    