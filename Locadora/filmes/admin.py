#coding:utf-8
from django.contrib import admin
from models import Cadfilme
from models import Cadfilme
from models import Precat
from models import Aluguel
from models import AlugelFlmes

class FimesalgInline(admin.TabularInline):
      model = AlugelFlmes
      extra = 1

# Register your models here.

class PrecatAdm(admin.ModelAdmin):
	list_display = ['Preco','Categ']
        list_filter = ['Categ']
        search_fields = ['Preco,','Categ']

class CadfAdm(admin.ModelAdmin):
	list_display = ['Nome','Gen','Nomed']
	list_filter = ['Gen','Cat']
        search_fields = ['Nome','Gen','Cat']

class AluguelAdm(admin.ModelAdmin):
      inlines = [FimesalgInline]
 
admin.site.register(Cadfilme,CadfAdm)
admin.site.register(Precat,PrecatAdm)
admin.site.register(Aluguel,AluguelAdm)
