from django.db import models
from django.contrib import admin
from django.utils import timezone, html
from django.utils.html import format_html
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model() # Создание модели пользователя

class Advertisement(models.Model): # это класс-модель обьявления
    # он реализует таблицу Advertisement
    title = models.CharField("заголовок", max_length=128)
    descriptoin = models.TextField("описание")
    price = models.FloatField("цена")
    auction = models.BooleanField("торг", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
    image = models.ImageField("изображение", upload_to="media/")

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @admin.display(description="дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span>Сегодня в {}</span>',
                create_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')
    
    @admin.display(description="дата обновления")
    def update_date(self):
        if self.updated_at.date() == timezone.now().date():
            update_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color:green; font-weight: bold"> Сегодня в {}</span>',
                update_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description='фото')
    def photo(self):
        if self.image:#проверяю что есть картинка
            return format_html(
                "<img src = '{}' width='100px' heigth = '100px' > ",
                self.image.url
            )
        return format_html(
                "<img src = 'http://127.0.0.1:8000/static/img/adv.png' width='100px'> heigth = '100px' ",
                
            )



    # представление в виде строки 
    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    # настройки для таблицы
    class Meta:
        db_table = 'advertisments' # переименовали таблицу 
        