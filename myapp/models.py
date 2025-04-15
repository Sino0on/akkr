from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "Базовая модель"
        verbose_name_plural = "Базовые модели"


class Sponsor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    logo = models.ImageField(upload_to='sponsors/', verbose_name="Логотип")
    website = models.URLField(blank=True, null=True, verbose_name="Веб-сайт")

    class Meta:
        verbose_name = "Спонсор"
        verbose_name_plural = "Спонсоры"

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    role = models.CharField(max_length=255, verbose_name="Роль")
    photo = models.ImageField(upload_to='team/', verbose_name="Фото")
    bio = models.TextField(blank=True, null=True, verbose_name="Биография")

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return f"{self.name} - {self.role}"


class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    file = models.FileField(upload_to='documents/', verbose_name="Файл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title


class ProjectCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Категория проекта"
        verbose_name_plural = "Категории проектов"

    def __str__(self):
        return self.name


class Project(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Слаг")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='projects/', verbose_name="Изображение")
    categories = models.ManyToManyField(ProjectCategory, related_name='projects', verbose_name="Категории")
    completed = models.BooleanField(default=False, verbose_name="Завершено")
    video_url = models.URLField(blank=True, null=True, verbose_name="Видео URL")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class NewsCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"

    def __str__(self):
        return self.name


class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    mini_title = models.CharField(max_length=255, verbose_name="Мини описание", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, verbose_name="Слаг")
    content = RichTextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="Изображение")
    categories = models.ManyToManyField(NewsCategory, related_name='news', verbose_name="Категории")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PublicationCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Категория публикации"
        verbose_name_plural = "Категории публикаций"

    def __str__(self):
        return self.name


class Publication(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Слаг")
    description = models.TextField(verbose_name="Описание")
    file = models.FileField(upload_to='publications/', verbose_name="Файл")
    # categories = models.ManyToManyField(PublicationCategory, related_name='publications', verbose_name="Категории")

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactMessage(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Message from {self.name}"


class Subscription(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return self.email


class SiteContent(models.Model):
    original_text = models.TextField(verbose_name="Оригинальный текст",
                                     help_text="Оригинальный текст, который отображается на сайте.",
                                     max_length=20000
                                     )
    current_text = models.TextField(
        verbose_name="Текущий текст",
        help_text="Измененный или текущий текст, который отображается на сайте.",
        max_length=20000
    )

    class Meta:
        verbose_name = "Контент сайта"
        verbose_name_plural = "Контент сайта"


class SingletonModel(models.Model):
    """
    Модель, которая всегда имеет только один экземпляр.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.__class__.objects.exists() and not self.id:
            existing = self.__class__.objects.first()
            for field in self._meta.fields:
                if field.name != 'id':
                    setattr(existing, field.name, getattr(self, field.name))
            existing.save()
        else:
            super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class AboutUs(SingletonModel):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    image1 = models.FileField(upload_to="images/", verbose_name='Первое изображение')
    image2 = models.FileField(upload_to="images/", verbose_name='Второе изображение')
    image3 = models.FileField(upload_to="images/", verbose_name='Третье изображение')
    title2 = models.CharField(max_length=255, verbose_name='Второе Название')
    description2 = RichTextField(verbose_name='Второе Описание')
    description3 = RichTextField(verbose_name='Третье Описание', blank=True, null=True)
    image4 = models.FileField(upload_to="images/", verbose_name='Четвертое изображение', blank=True, null=True)

    def __str__(self):
        return "О нас"

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Contacts(SingletonModel):
    address = models.CharField(max_length=255, verbose_name="Адрес", blank=True, default='')
    link_address = models.TextField(verbose_name="Ccылка на адрес", blank=True, default='')
    phone = models.CharField(max_length=123, verbose_name="Номер телефона", default='')
    email = models.EmailField(max_length=123, verbose_name='Почта', default='22116708')

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return "Контакты"

class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", blank=True, default='')
    slug = models.SlugField(unique=True, blank=True, verbose_name="Слаг")
    description = RichTextField(verbose_name='Описание')
    categories = models.ManyToManyField(PublicationCategory, related_name='publications', verbose_name="Категории")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']


class MorePage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", blank=True, default='')
    mini_title = models.CharField(max_length=255, verbose_name="Цель", blank=True, default='')
    slug = models.SlugField(unique=True, blank=True, verbose_name="Слаг")
    description = RichTextField(verbose_name='Описание')
    # categories = models.ManyToManyField(PublicationCategory, related_name='publications', verbose_name="Категории")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['created_at']


choise = (
    ('image', 'image'),
    ('file', 'file'),
)


class PageImage(models.Model):
    image = models.FileField(upload_to='images/')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='images_page')
    name = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=123, choices=choise, blank=True, default='image')

    def __str__(self):
        return f'{self.page}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class MorePageImage(models.Model):
    image = models.FileField(upload_to='images/')
    more_page = models.ForeignKey(MorePage, on_delete=models.CASCADE, related_name='images_page')

    def __str__(self):
        return f'{self.more_page}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'



class Application(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


class GalleryImage(models.Model):
    title = models.CharField(max_length=123, blank=True, null=True)
    image = models.FileField(upload_to='gallery')
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']
