from django.contrib import admin
from .models import customer_tmaskpl, srodowisko_tmaskpl

# @admin.register(customer_tmaskpl)
class AnsibleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Nazwa', {
            'fields': ('customer_name','customer_skrot_firmy',),
            'description': 'Nazwa firmy',
            'classes': ('collapse',),
        }),
        ('Adres', {
            'fields': ('customer_miasto','customer_kod_pocztowy','customer_ul','customer_nr_lok',),
            'description': 'Adres firmy',
            'classes': ('collapse',),
        }),
        ('Kontakt', {
            'fields': ('customer_telefon','customer_email',),
            'description': 'Kontakt do firmy',
            'classes': ('collapse',),
        }),
        ('Socialmedia', {
            'fields': ('customer_github','customer_facebook','customer_linkedin',),
            'description': 'Socialmedia',
            'classes': ('collapse',),
        }),
        ('Inne', {
            'fields': ('customer_opis','customer_srodowisko','customer_upload',),
            'description': 'Inne',
            'classes': ('collapse',),
        }),
    )
    # fields = ["customer_skrot_firmy"]
    # exclude = ['customer_facebook']
    # list_display = ["customer_name", "customer_miasto", "customer_telefon", "customer_email"]
    # list_filter = ("customer_miasto",)
    # search_fields = ["customer_name", "customer_opis"]
    
admin.site.register(customer_tmaskpl, AnsibleAdmin)
