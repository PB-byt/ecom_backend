from django.db import models

# Create your models here.
color_grade = [ ('sd_wht', 'only white piece'), ('sd_col', 'one color piece'), ('mx_col', 'mixed color piece') ]
usage = [('nk','NECKLACE'),('hd','BRACELET'),('bag','MULTI PURPOSE BAG'),('others','ACCESSORIES')]

class Product(models.Model):
    name =models.CharField(max_length=40)
    price = models.IntegerField(default= 0,help_text = 'enter product price here')
    added_in = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=160)
    rcg_tag = models.CharField(max_length = 25,choices = color_grade,default = 'mx_col')
    type = models.CharField(max_length=15,choices=usage,default='hd')
    face_pic = models.ImageField(upload_to='face_photos',default = 'none') # newly added field for product card pics in overview section

    # def face_pics(self): # the self word can be treated as the instance itself
    #     return self.photos.get(pk=1) # this return the query set containing picture object,
                                     # in case of .all() - get picture objects as needed get by using id , thus you would reach to a single object; on;y then .pic() method is usable


class Pictures(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='photos')
    pic = models.ImageField(upload_to = 'product_photos')

# making changes in existing models -- only migrate command is enough, but in case of making new models make migrations command in necessery
# other wise it will not work in admin panel