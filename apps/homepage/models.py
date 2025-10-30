from django.db import models

class Homepage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    file = models.FileField(upload_to='homepage_files/', verbose_name="Файл", null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Главной страницы"
        verbose_name_plural = "Главной страницы"

class Statistics(models.Model):
    users_count = models.PositiveIntegerField(verbose_name="Пользователей")
    bought_products_count = models.PositiveIntegerField(verbose_name="Купили товары")
    total_products_count = models.PositiveIntegerField(verbose_name="Всего товаров")

    def __str__(self):
        return f"Статистика: {self.users_count} пользователей"
    
    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"


class HeaderFooter(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    bottom_text = models.CharField(max_length=200, verbose_name="Нижний текст")
    top_logo = models.ImageField(upload_to='footer/logos/', verbose_name="Верхний логотип", blank=True, null=True)
    bottom_logo = models.ImageField(upload_to='footer/logos/', verbose_name="Верхний логотип", blank=True, null=True)
    instagram = models.URLField(max_length=200, verbose_name="Instagram URL", blank=True, null=True)
    telagram = models.URLField(max_length=200, verbose_name="Telegram URL", blank=True, null=True)
    vk = models.URLField(max_length=200, verbose_name="VK URL", blank=True, null=True)
    
    class Meta:
        verbose_name = "Верхний и нижний колонтитул"
        verbose_name_plural = "Верхний и нижний колонтитул"

class Partner(models.Model):
    footer = models.ForeignKey(HeaderFooter, on_delete=models.CASCADE, related_name='partners')
    name = models.CharField(max_length=100, verbose_name="Название партнера")
    
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

class Brand(models.Model):
    footer = models.ForeignKey(HeaderFooter, on_delete=models.CASCADE, related_name='brands')
    name = models.CharField(max_length=100, verbose_name="Название бренда")
    
    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

class Sections(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название секции")
    description = models.TextField(verbose_name="Описание секции", blank=True, null=True)
    image = models.ImageField(upload_to='sections/images/', verbose_name="Изображение секции", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"

class Content(models.Model):
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=200, verbose_name="Заголовок содержания")
    description = models.TextField(verbose_name="Описание содержания")
    image = models.ImageField(upload_to='contents/images/', verbose_name="Изображение содержания", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Содержание"
        verbose_name_plural = "Содержания"