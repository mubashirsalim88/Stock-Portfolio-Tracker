from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from .forms import StockForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect
from .forms import StockForm
from django.contrib.auth.decorators import login_required

@login_required
def portfolio_view(request):
    stocks = Stock.objects.filter(user=request.user)
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
            return redirect('portfolio_view')
    else:
        form = StockForm()

    return render(request, 'portfolio/portfolio.html', {'stocks': stocks, 'form': form})


@login_required
def delete_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id, user=request.user)
    stock.delete()
    return redirect('portfolio_view')



@login_required
def update_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id, user=request.user)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock updated successfully!')
            return redirect('portfolio_view')
    else:
        form = StockForm(instance=stock)

    return render(request, 'portfolio/update_stock.html', {'form': form})



@login_required
def portfolio_view(request):
    stocks = Stock.objects.filter(user=request.user)
    return render(request, 'portfolio/portfolio.html', {'stocks': stocks})



from django.contrib import messages

@login_required
def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
            messages.success(request, 'Stock added successfully!')
            return redirect('portfolio_view')
    else:
        form = StockForm()
    return render(request, 'portfolio/add_stock.html', {'form': form})

