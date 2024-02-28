from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from .forms import CSVImportForm
from .models import Book
import csv
from django.core.management import call_command
from django.views.generic import ListView

def home(request):
    return render(request, 'home.html')


def export_csv(request):
    # Your data retrieval logic goes here
    data = [
        ['Name', 'Age', 'Email'],
        ['John Doe', 30, 'john@example.com'],
        ['Jane Smith', 25, 'jane@example.com'],
        # Add your data here
    ]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'

    writer = csv.writer(response)
    for row in data:
        writer.writerow(row)

    return response


def export_query_to_csv(request):
    data = Book.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name*', 'Kategorie', 'Verkaufspreis Brutto*'])  # CSV header

    for Book in data:
        writer.writerow([Book.Name, Book.Kategorie, Book.Verkaufspreis])

    return response


def export_html_to_csv(request):
    html = """
    <!-- Your HTML table content here -->
    """
    soup = BeautifulSoup(html, 'html.parser')
    data = []

    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        data.append([col.text for col in cols])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="/table_data.csv"'

    writer = csv.writer(response)
    for row in data:
        writer.writerow(row)

    return response


# views.py


def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES, )
        if form.is_valid():
            call_command('flush', interactive=False)
            #Book.objects.all().delete()
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file, delimiter=";")

            for row in csv_reader:
                Book.objects.create(
                    Name=row['\ufeffName*'],
                    Kategorie=row['Kategorie'],
                    Verkaufspreis=row['Verkaufspreis Brutto*'],
                )

            return redirect('home')  # Redirect to a success page
    else:
        form = CSVImportForm()
    
    return render(request, 'import.html', {'form': form})



class menue(ListView):
    model = Book
    template_name = "index.html"

class menue_filter(ListView):
    model = Book
    template_name = "bier.html"

    def get_queryset(self):
        bier = Book.objects.filter(Kategorie="Bier")
        return bier
