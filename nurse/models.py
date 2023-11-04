from django.db import models

# Create your models here.
# we need to create costom user model which contains
# Форма собственности
# ИНН организации
# Наименование организации
# ПИН руководителя
# ФИО руководителя
# Должность
# Электронная почта
# Веб-сайт (если имеется)
# Населённый пункт
# Город/Село/Айыл окмот
# Юридический адрес
# улица № дома
# Фактический адрес

class Costom_User(models.Model):
    form_soobsh = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pint_head = models.CharField(max_length=100)
    name_head = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    settlement = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    ur_address = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    fact_address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# creating comment model so one user can comment to another user
class Comment(models.Model):
    user_from = models.ForeignKey(Costom_User, on_delete=models.CASCADE)
    user_to = models.ForeignKey(Costom_User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    