from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    date = models.IntegerField(verbose_name="Дата рождения")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
    
    def __str__(self):
        return f'{self.name} {self.lastname}'

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    name = models.CharField(max_length=100, verbose_name="Название")
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    date = models.IntegerField(verbose_name="Год создания")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
    
    def __str__(self):
        return self.title
    


