from django.db import models

# หมวดหมู่ค่ําใช้จ่ายที่ฟิกไว้
CATEGORY_CHOICES = [
    ('อาหาร', 'อาหาร'),
    ('เครื่องดื่ม', 'เครื่องดื่ม'),
    ('เดินทาง', 'เดินทาง'),
    ('ที่พัก', 'ที่พัก'),
    ('ช้อปปิ้ง', 'ช้อปปิ้ง'),
    ('อื่นๆ', 'อื่นๆ'),
]

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # จำนวนเงิน
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # หมวดหมู่
    note = models.TextField(blank=True, null=True)  # หมายเหตุ
    date = models.DateField()  # วันที่ใช้จ่าย

    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount}"
