from django.shortcuts import render, HttpResponse, redirect
from .models.product import Product
from .models.category import Category
from .models.orders import Orders
from .models.contact import Contact
# first import this for Pagination and then write code in home function
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic.list import ListView  # for ListView class-BlogHome
from django.contrib.auth.models import User


# Create your views here.
class HomeView(ListView):
    model = Product  # that means Post.objects.all()
    template_name = "shop/index.html"
    ordering = ['id']  # ordering for pagination

    # for pagination, we need only 1 command other by internal work, paginate_by=2, and all same in template like function based view
    paginate_by = 16
    # paginate_orphans = 2 #for adjusting last page
    context_object_name = "allItems"


def search(request):
    categories = Category.objects.all()

    # fetching data by category id
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)

        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    else:
        products = Product.objects.all()

        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    # search results logic
    query = request.GET['query']

    if len(query) > 78 or query == '':
        allProducts = Product.objects.none()

    else:
        allProducts = Product.objects.filter(product_name__icontains=query)

    if allProducts.count() == 0:
        messages.warning(request, "No search results found: Please refine your query")

    params = {'allProducts': allProducts, 'query': query, 'categories': categories, 'page_obj': page_obj}
    return render(request, 'shop/search.html', params)


def shop(request):
    # product = Product.get_all_products() # in case of get product in models and retrive there
    # products = Product.objects.all().order_by('-id')  #in case of pagination, we use '-title' not 'title' for getting latest object

    #####Pagination for Functin based view####
    # data must be in order otherwise it will show error and import Paginator
    # paginator = Paginator(post_list, 2, orphans=1) #orphans=1, because it adjust last post
    model = Product.objects.all()
    categories = Category.objects.all()

    # fetching data by category id
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID).order_by('-id')

        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    else:
        products = Product.objects.all().order_by('-id')

        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'categories': categories, 'model': model}
    return render(request, "shop/shop.html", context)


def detail(request, id):
    # fetch product id there, use session for add item in dictionary
    if request.method == "POST":
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        # print(product)
        # now save this id in dictionary as a session
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)

            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])

    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}

    data = Product.objects.filter(id=id).first()

    context = {'data': data}
    return render(request, "shop/detail.html", context)


def cart(request):
    # get cart by request.session.get('cart')
    # print(request.session.get('cart').keys())
    #ids = list(request.session.get('cart').keys())
    #products = Product.objects.filter(id__in=ids)
    # print(products)
    # we create filter for quantity by using cart_quantity through cart.py
    if request.session.get('cart') == None:
        return render(request, "shop/cart.html")
    else:
        ids = list(request.session.get('cart').keys())
        products = Product.objects.filter(id__in=ids)
        context = {'products': products}
        return render(request, "shop/cart.html", context)

def checkout(request):
    ids = list(request.session.get('cart').keys())
    products = Product.objects.filter(id__in=ids)
    if request.method == "POST":
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        # get other filed by session
        cart = request.session.get('cart')
        ids = list(request.session.get('cart').keys())
        products = Product.objects.filter(id__in=ids)
        customer = request.user

        # Place order, first import order
        for product in products:
            order = Orders(customer=customer, product=product, price=product.price, address=address,
                           phone=phone, quantity=cart.get(str(product.id)))
            order.save()
            messages.success(request, "Thanks for Shopping, please check order status in Orders page")
        request.session['cart'] = {}
        print(phone)
        print(address)
        print(customer)
        print(cart)
        print(products)

        return redirect('cart')
    return render(request, "shop/checkout.html", {'products':products})

def order(request):
    if request.user.is_authenticated:  # this is middleware for default django user
        customer = request.user
        order = Orders.objects.filter(customer_id=customer).order_by('-date') #order_by for des order

        paginator = Paginator(order, 6)
        page_number = request.GET.get('page')
        orders = paginator.get_page(page_number)

        print(orders)
        context = {'orders': orders}
        return render(request, "shop/orders.html", context)
    else:
        return redirect('/login/')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(message)<10:
            messages.success(request, "Please Fill the Form Correctly")
        else:
            # store in database
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request, "Your Message has been successfully sent")
    return render(request, 'shop/contact.html')


def about(request):
    return HttpResponse("This is About Page")
