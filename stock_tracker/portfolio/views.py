from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from .forms import StockForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def portfolio_view(request):
    stocks = Stock.objects.filter(user=request.user)

    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
            messages.success(request, 'Stock added successfully!')
            return redirect('portfolio_view')  # Redirect to the same view to display stocks
    else:
        form = StockForm()

    return render(request, 'portfolio/portfolio.html', {'stocks': stocks, 'form': form})

@login_required
def delete_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id, user=request.user)
    stock.delete()
    messages.success(request, 'Stock deleted successfully!')
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

@login_required
def index_view(request):
    return render(request, 'portfolio/index.html')


@login_required
def index_view(request):
    stocks = Stock.objects.filter(user=request.user)  # Fetch stocks for the logged-in user
    
    total_value = sum(stock.current_price * stock.quantity for stock in stocks if stock.current_price is not None)  # Ensure current_price is not None
    daily_change = sum(stock.daily_change for stock in stocks if stock.daily_change is not None)  # Ensure daily_change is not None
    stock_count = stocks.count()

    context = {
        'stocks': stocks,
        'total_value': total_value,
        'daily_change': daily_change,
        'stock_count': stock_count,
    }
    return render(request, 'portfolio/index.html', context)  # Ensure this path matches your template structure

