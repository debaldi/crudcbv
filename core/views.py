from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto


class IndexView(ListView):
    models = Produto
    # Nome do Template
    template_name = 'index.html'
    # queryset - Busca
    queryset = Produto.objects.all()
    # 'produtos' - é o for da página index
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    # Model
    model = Produto
    # Nome do Template
    template_name = 'produto_form.html'
    # Nome dos Campos
    fields = ['nome', 'preco']
    # success_url - Para onde vai ser direcionado caso de certo
    # ('index') - Nome da rota
    # reverse_lazy - Verefica qual a view da Rota e direciona para ('index')
    success_url = reverse_lazy('index')


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')
