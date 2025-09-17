from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

# หน้าแสดงค่าใช้จ่ายทั้งหมด + ฟอร์มเพิ่มรายการ
def index(request):
    expenses = Expense.objects.all().order_by('-date')  # เรียงตามวันที่ล่าสุด

    # filter ตามวันที่ถ้ามี
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        expenses = expenses.filter(date__range=[start_date, end_date])

    # สรุปผลรวมรายจ่ายทั้งหมด
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    # เพิ่มรายการใหม่
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()

    context = {
        'expenses': expenses,
        'form': form,
        'total_expense': total_expense,
        'start_date': start_date or '',
        'end_date': end_date or '',
    }
    return render(request, 'index.html', context)

# แสดงใบเสร็จทุกรายการ
def receipts(request):
    expenses = Expense.objects.all().order_by('-date')
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'expenses': expenses,
        'total_expense': total_expense,
    }
    return render(request, 'receipts.html', context)