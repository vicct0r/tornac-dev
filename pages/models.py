from django.db import models
from stdimage import StdImageField


class Tag(models.Model):
    nome = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return self.nome


class Aplicativo(models.Model):
    CONCLUIDO = 'cm'
    DESENVOLVIMENTO = 'ds'

    ESTADOS_STATUS_CHOICES = (
        (CONCLUIDO, 'Concluído'),
        (DESENVOLVIMENTO, 'Em Desenvolvimento')
    )
    
    criado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    titulo = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=ESTADOS_STATUS_CHOICES, default=DESENVOLVIMENTO)
    descricao = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='taged', blank=True, null=True)
    categoria = models.CharField(max_length=150)
    url = models.URLField(blank=True, null=True)
    repositorio = models.URLField(blank=True, null=True)
    imagem = StdImageField(
        upload_to='projetos/',
        variations={
            'card': {
                'width': 400,
                'height': 200,
                'crop': True
            },
            'thumbnail': {
                'width': 100,
                'height': 100,
                'crop': True
            }
        },
        delete_orphans=True,
        blank=True,
        null=True,
        help_text="Imagem do projeto (400x200px recomendado)"
    )


    def __str__(self):
        return f"{self.titulo}"