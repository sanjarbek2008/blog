from django.db import models
from django.contrib.auth.models import User


class BlogCategories(models.Model):
    name = models.CharField(max_length=255, verbose_name='kategoriya nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog kategoriyasi"
        verbose_name_plural = "Bloglar kategoriyalari"
        ordering = "id",


class PassportInfo(models.Model):
    firstname = models.CharField(max_length=255, verbose_name="ism")
    lastname = models.CharField(max_length=255, verbose_name="familiya")
    age = models.PositiveSmallIntegerField(verbose_name="yosh")
    seria = models.CharField(max_length=2)
    number = models.CharField(max_length=10)


class Author(models.Model):
    STATUS = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('super admin', 'Bosh admin')
    )
    info = models.OneToOneField(PassportInfo, verbose_name='Passport malumotlari', on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=STATUS, max_length=50, default='manager')

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "ega"
        verbose_name_plural = "egalar"


class BlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='accepted')



class Blog(models.Model):
    STATUS = (
        ('create', 'yaratilgan'),
        ('accepted', 'tasdiqlangan'),
        ('cancelled', 'bekor qilingan')
    )
    category = models.ForeignKey(BlogCategories, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300, verbose_name='sarlavha')
    short_description = models.TextField(verbose_name="qisqa izoh")
    description = models.TextField(verbose_name="izoh")
    photo = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana', null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True,null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='created')
    objects = models.Manager()
    blog_manager = BlogManager()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"
        ordering = ["id"]































