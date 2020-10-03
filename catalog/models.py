from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
	('Men','Men'),
	('Electronics','Electronics'),
	('Cars','Cars'),
	('Food','Food'),
	('Books','Books'),
	('Shoe','Shoe')
)

LABEL_CHOICES = (
	('S','secondary'),
	('P','primary'),
	('D','danger')
)

class Item(models.Model):
	title = models.CharField(max_length=200)
	price = models.IntegerField()
	discount_price = models.IntegerField(blank=True, null=True)
	slug =  models.SlugField()
	status = models.CharField(max_length=200)
	category = models.CharField(choices=CATEGORY_CHOICES,max_length=15)
	label  = models.CharField(choices=LABEL_CHOICES,max_length=2)
	description = models.TextField()
	image = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100,default='default.jpg')

	def __str__(self):
		return self.title

	def get_add_to_cart_url(self):
		return reverse( 'add_to_cart',kwargs={'slug':self.slug})

	def get_remove_from_cart_url(self):
		return reverse( 'remove_from_cart',kwargs={'slug':self.slug})



class OrderItem(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Item,on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.quantity} of {self.item.title}"

	def get_total_item_price(self):
		return self.quantity * self.item.price

	def get_amount_saved(self):
		return self.get_total_item_price() - self.get_final_price()


	def get_total_item_discount_price(self):
		return self.quantity * self.item.discount_price

	def get_final_price(self):
		if self.item.discount_price:
			return self.get_total_item_discount_price()
		return self.get_total_item_price()


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	ordered = models.BooleanField(default=False)
	start_date = models.DateTimeField( auto_now_add=True)
	ordered_date = models.DateTimeField()

	def __str__(self):
		return self.user.username

def get_total(self):
	total = 0
	for order_item in self.items.all():
		total +=order_item.get_final_price()
	return total

class slider(models.Model):
	image = models.ImageField(upload_to='slider')
	slug =  models.SlugField(default='item')
	category = models.CharField(choices=CATEGORY_CHOICES,max_length=15,default='Food')


class addition_info(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	slug =  models.SlugField(default='Food')
	images = models.ImageField(upload_to='addition_info')
	descriptions = models.TextField(blank=True)

class about(models.Model):
	image = models.ImageField(upload_to='about')
	title1 =  models.CharField(max_length=200)
	description1 =  models.TextField()
	title2 =  models.CharField(max_length=200)
	description2 =  models.TextField()

class about1(models.Model):
	image = models.ImageField(upload_to='about')

