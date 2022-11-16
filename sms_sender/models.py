import django
from django.db import models
from django.core.validators import RegexValidator


class Tag(models.Model):
    name = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='Тег'
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)


class Operator(models.Model):
    class Meta:
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'
        ordering = ('name',)

    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)


class Dispatch(models.Model):
    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    start_dt = models.DateTimeField(null=False,
                                    verbose_name='Дата и время начала рассылки'
                                    )

    stop_dt = models.DateTimeField(null=False,
                                   verbose_name='Дата и время окончания рассылки'
                                   )

    text = models.CharField(max_length=100,
                            verbose_name='Текст рассылки'
                            )
    tags = models.ManyToManyField(Tag)
    operators = models.ManyToManyField(Operator)

    def __str__(self):
        return f'Рассылка {self.id}:{self.start_dt}:{self.text}'


class Client(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    valid_p_number = RegexValidator(regex=r'^7\w{10}$',
                                    message='проверка мобильного телефона'
                                    )

    p_number = models.CharField(max_length=11,
                                unique=True,
                                verbose_name='Мобильный телефон',
                                validators=[valid_p_number]
                                )

    operator_code = models.CharField(max_length=3,
                                     verbose_name='Оператор клиента')

    tag = models.CharField(max_length=15,
                           verbose_name='Тег')

    timezone = models.IntegerField(verbose_name='Часовой пояс GMT+')

    def save(self, *args, **kwargs):
        tag_name = self.tag
        op_name = self.operator_code
        self.operator_code, created = Operator.objects.get_or_create(name=op_name)
        self.tag, created = Tag.objects.get_or_create(name=tag_name)
        super().save()

    def __str__(self):
        return f'Клиент {self.id}:{self.p_number}:{self.tag}:{self.timezone}'


class Message(models.Model):
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    SENT = 'Отправлено'
    NOT_SENT = 'Не отправлено'
    STATUS = [
        (SENT, 'Отправлено'),
        (NOT_SENT, 'Не отправлено')
    ]

    status = models.CharField(max_length=15,
                              choices=STATUS,
                              default=NOT_SENT,
                              verbose_name='статус сообщения'
                              )

    send_dt = models.DateTimeField(default=django.utils.timezone.now(),
                                   verbose_name='Дата и время отправки'
                                   )
    client_id = models.ForeignKey(Client,
                                  on_delete=models.CASCADE,
                                  verbose_name='ИД клиента'
                                  )
    dispatch_id = models.ForeignKey(Dispatch,
                                    on_delete=models.CASCADE,
                                    verbose_name='ИД рассылки'
                                    )

    def __str__(self):
        return f'Сообщение {self.id}:{self.client_id}:{self.dispatch_id}:{self.status}'
