from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField




class StatusChoices(models.TextChoices):
    NEW = 'New', _('Yangi')
    IN_PROGRESS = 'In Progress', _('Tayyorlanmoqda')
    READY = 'Ready', _('Tayyor')

class Worker(models.Model):
    name = models.CharField(_('Ismi'), max_length=255)
    role = models.CharField(_("Ro'li"), max_length=50, choices=[
        ('Mix ustasi', _('Mix ustasi')),
        ("Yog'och ustasi", _("Yog'och ustasi")),
        ('Sintafon ustasi', _('Sintafon ustasi'))
    ])
    tasks = models.TextField(_('Vazifalar'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Ishchi"
        verbose_name = _("Ishchi")
        verbose_name_plural = _("Ishchilar")

class RawMaterial(models.Model):
    name = models.CharField(_('Nomi'), max_length=255)
    quantity = models.IntegerField(_('Miqdori'))
    image = ResizedImageField(size=[800, 800], upload_to='raw_materials/images/', verbose_name=_('Rasmi'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Hom-ashyolar"
        verbose_name = _("Hom-ashyolar")
        verbose_name_plural = _("Hom-ashyolar")

class Customer(models.Model):
    name = models.CharField(_('Nomi'), max_length=255)
    contact_info = models.TextField(_("Aloqa ma'lumotlari"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Mijoz"
        verbose_name = _("Mijoz")
        verbose_name_plural = _("Mijozlar")

class Order(models.Model):
    name = models.CharField(_('Nomi'), max_length=255)
    deadline = models.DateTimeField(_('Deadline'))
    workers = models.ManyToManyField('Worker', through='OrderWorker', related_name='orders', verbose_name=_('Ishchilar'))
    price = models.FloatField(_('Narxi'))
    information = models.TextField(_("Ma'lumot"))
    type = models.CharField(_('Turi'), max_length=100)
    image = ResizedImageField(size=[800, 800], upload_to='orders/images/', verbose_name=_('Rasmi'))
    status = models.CharField(_('Holati'), max_length=50, choices=StatusChoices.choices, default=StatusChoices.NEW)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True, related_name='orders', verbose_name=_('Buyurtmachi'))
    raw_materials = models.ManyToManyField('RawMaterial', related_name='orders', verbose_name=_('Hom-ashyo'))
    comments = models.TextField(_('Izohlar'), null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Zakaz"
        verbose_name = _("Zakaz")
        verbose_name_plural = _("Zakazlar")

class OrderWorker(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE)
    task = models.TextField(_('Vazifasi'))

    class Meta:
        db_table = "ZakazIshchilar"
        verbose_name = _("Zakaz-Ishchi")
        verbose_name_plural = _("Zakaz-Ishchilar")

class FinishedProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='finished_product')
    quantity = models.IntegerField(_('Miqdori'))
    image = ResizedImageField(size=[800, 800], upload_to='products/images/', verbose_name=_('Rasmi'))
    workers = models.ManyToManyField('Worker', related_name='finished_products', verbose_name=_('Ishchilar'))

    def __str__(self):
        return f"Tayyor mahsulot: {self.order.name}"

    class Meta:
        db_table = "Tayyor-Mahsulot"
        verbose_name = _("Tayyor-Mahsulot")
        verbose_name_plural = _("Tayyor-Mahsulotlar")
