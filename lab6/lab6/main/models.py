from django.db import models
class Sotrudnik(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    data_birth = models.DateField('Дата рождения')
    stazh = models.IntegerField('Стаж')
    def __str__(self):
        return f'Сотрудник:{self.surname}'

    def get_absolute_url(self):
        return f'/update_sotr/{self.id}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'



class Clients(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    data_birth = models.DateField('Дата рождения')
    email = models.EmailField('Почта')

    def __str__(self):
        return f'Клиент:{self.surname}'

    def get_absolute_url(self):
        return f'/update_client/{self.id}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Bank(models.Model):
    surname = models.CharField('Фамилия',max_length=50)
    name = models.CharField('Имя',max_length=50)
    date_and_time = models.DateTimeField('Дата посещения')
    service = models.CharField('Услуга', max_length=50)
    sotrudnik = models.OneToOneField(Sotrudnik, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Клиент:{self.surname}'

    def get_absolute_url(self):
        return f'/update_bank/{self.id}'

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

class Credit(models.Model):
    client =  models.ForeignKey(Clients, on_delete=models.CASCADE)
    summa = models.IntegerField('Сумма')
    procent = models.IntegerField('Процент')
    years = models.IntegerField('Лет')
    def __str__(self):
        return f'Кредит:{self.client}'

    def get_absolute_url(self):
        return f'/update_credit/{self.id}'

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'


class Count(models.Model):
    client = models.OneToOneField(Clients, on_delete=models.CASCADE)
    summa = models.IntegerField('Сумма')

    def __str__(self):
        return f'Счет:{self.client}'

    def get_absolute_url(self):
        return f'/update_count/{self.id}'

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

class Dolzhnost(models.Model):
    name = models.CharField('Должность',max_length=50)
    sotrudnik = models.ManyToManyField(Sotrudnik)

    def __str__(self):
        return f'Должность:{self.name}'

    def get_absolute_url(self):
        return f'/update_dolzh/{self.id}'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'