from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Member
from .model2 import Products
from .model2 import Customers
from .model2 import Orders
from .model2 import Cart
from django.template import loader
def members(request):
    return HttpResponse("Hello World!!!")
def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())
def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def log(request):
    f=request.GET["first"]
    l=request.GET["last"]
    mydata=Member.objects.filter(name=f,password=l).values()
    
    if not mydata:
        return HttpResponse("User Not Found")
    #return HttpResponse(mydata)
    memid=mydata[0]['memid']
    template=loader.get_template('display.html')
    context={
        'cid':memid,
        'name':f,
    }
    return HttpResponse(template.render(context,request))
def sign(request): 
    f=request.GET["fname"]
    l=request.GET["lname"]
    mob=request.GET["number"]
    addr=request.GET["Address"]
    mydata=Member.objects.filter(name=f,password=l).values()
    if  mydata:
        return HttpResponse("user already exists")
    mymember=Member(name=f,password=l,mobile=mob,address=addr)
    mymember.save()
    return HttpResponse('Data Saved')
def products(request):
    id=request.GET["userid"]
    mydata=Products.objects.all().values()
    template=loader.get_template('products.html')
    context={
        'mydata':mydata,
        'cid':id,
    }
    return HttpResponse(template.render(context,request))
def customer(request):
   id=request.GET["userid"]
   productid=request.GET["productid"]
   mydata=Orders.objects.filter(custid=id,oid=productid).values()
   myproducts=Products.objects.filter(proid=productid).values()
   oname=myproducts[0]['proname']
   q=0
   if  mydata:
      q=mydata[0]['quantity']
   cust=Orders(custid=id,oid=productid,quantity=q+1,oname=oname)
   cust.save()
   return HttpResponse("Order Placed Successfully!!")

def myorders(request):
    id=request.GET["userid"]
    mydata=Orders.objects.filter(custid=id).values()
    myproducts=Products.objects.all().values()
    #return HttpResponse(mydata)
    if not mydata:
        return HttpResponse("No Orders")
    template=loader.get_template('myorders.html')
    context={
        'mydata':mydata,
        'myproducts':myproducts,
    }
    return HttpResponse(template.render(context,request))
def cart(request):
    id=request.GET["userid"]
    proid=request.GET["productid"]
    quantity=request.GET["quantity"]
    mydata=Cart.objects.filter(cid=id,proid=proid).values()
    myproducts=Products.objects.filter(proid=proid).values()
    proname=myproducts[0]['proname']
    q=0
    if mydata:
        q=mydata[0]['quantity']
    c=Cart(cid=id,proid=proid,quantity=q+1,proname=proname)
    c.save()
    return HttpResponse("Added to Cart")
def show(request):
    id=request.GET["userid"]
    proid=request.GET["productid"]
    mydata=Products.objects.filter(proid=proid).values()
    template=loader.get_template("show.html")
    context={
        'cid':id,
        'pimg':mydata[0]['pimg'],
        'proid':mydata[0]['proid'],
        'q':mydata[0]['quantity'],
        'price':mydata[0]['price'],
        'proname':mydata[0]['proname'],
    }
    return HttpResponse(template.render(context,request))
def showcart(request):
    id=request.GET["userid"]
    mydata=Cart.objects.filter(cid=id).values()
    if not mydata:
        return HttpResponse("No Items In Cart")
    template=loader.get_template('cart.html')
    context={
        'mydata':mydata,
    }
    return HttpResponse(template.render(context,request))
def account(request):
    id=request.GET["userid"]
    mydata=Member.objects.filter(memid=id).values()
    template=loader.get_template("Account.html")
    context={
        'id':mydata[0]['memid'],
        'name':mydata[0]['name'],
        'mob':mydata[0]['mobile'],
        'addr':mydata[0]['address'],
    }
    return HttpResponse(template.render(context,request))
def logout(request):
    return HttpResponseRedirect('/login')


    