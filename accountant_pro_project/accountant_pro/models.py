from django.db import models
from django.contrib.auth.models import User

from datetime import date
import uuid


class Currency(models.Model):
    name = models.CharField(max_length=20)
class Company(models.Model):
    name = models.CharField(max_length=255)
    default_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, default=1)
class CompanyDetail(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=8)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class BankAccount(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_amount = models.IntegerField()
    name = models.CharField(max_length=200)
    iban = models.CharField(max_length=34)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)


class Client(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    company = models.ForeignKey(Company, related_name='client_details', on_delete=models.PROTECT)


class ClientDetail(models.Model):
    client = models.OneToOneField(Client, related_name='details', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=8)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    vat = models.CharField(max_length=200)
    commerce = models.CharField(max_length=200)


class ClientAccount(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Invoice(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    reference = models.CharField(max_length=35)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)


class Item(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    description = models.TextField()
    default_price = models.DecimalField(decimal_places=2, max_digits=20)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='invoice_item_item', on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    amount = models.IntegerField()


class InvoiceViewed(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)


class InvoicePaid(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)


class InvoiceSent(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    company = models.ForeignKey(Company, related_name='vendor_details', on_delete=models.PROTECT)


class VendorDetail(models.Model):
    vendor = models.OneToOneField(Vendor, related_name='details', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=8)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    vat = models.CharField(max_length=200)
    commerce = models.CharField(max_length=200)


class Bill(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    date = models.DateField(default=date.today)
    reference = models.CharField(max_length=35)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='bill_item_item', on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    amount = models.IntegerField()
