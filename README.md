[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UnsbxNfJ)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16127198&assignment_repo_type=AssignmentRepo)
# Tugas 2: Menambah Data Dinamis ke Website Personal Anda dengan Django
## Tujuan Tugas:
Dalam tugas ini, Anda akan belajar cara menambahkan data dinamis ke dalam website personal yang telah Anda bangun sebelumnya. Anda akan fokus memahami **models**, **views**, **urls**, dan **templates** di Django, serta bagaimana menampilkan data dari database ke dalam halaman web.

## Petunjuk Tugas:
### Perubahan yang diinginkan:
Berikut adalah daftar perubahan yang diinginkan pada website personal Anda yang telah Anda bangun sebelumnya:
1. Mengelola Profil and Resume ke dalam database.
2. Menampilkan data profil dan resume ke dalam halaman web.
3. Mengelola data proyek yang pernah dikerjakan ke dalam database.
4. Menampilkan data proyek ke dalam halaman web.
5. Menambahkan halaman detail untuk setiap proyek yang menampilkan informasi lebih lengkap.
6. Mengelola data kontak ke dalam database.
7. Menampilkan halaman response ketika pengunjung mengirimkan pesan melalui form kontak. Response tersebut harus berisi informasi yang dikirim oleh pengunjung, ucapkan terima kasih, dan informasi bahwa pesan telah terkirim dan akan ditindaklanjuti segera.

### Persiapan Tugas
1. Tugas ini merupakan kelanjutan dari tugas sebelumnya, yaitu
   - Class X [Tugas 1: Membangun Website Statis dengan Django](https://classroom.google.com/c/NzA1NTYwODc2MDA4/a/NzE4MDAzODk3MzA5/details).
   - Kelas B [Tugas 1: Membangun Website Statis dengan Django](https://classroom.google.com/c/NzA1NTYzMDE1MDc0/a/NzExOTY5NjE0ODc1/details).
   - Kelas D [Tugas 1: Membangun Website Statis dengan Django](https://classroom.google.com/c/NzA1NTYyNTczNzQz/a/NzA1ODI4MDM2OTA4/details).
2. Kali ini kita akan menggunakan Github Classroom untuk mengelola tugas ini. 


## Langkah-langkah Tugas:
### Langkah 1: Memecah aplikasi `webapp` menjadi beberapa aplikasi, yakni: `profile`, `projects`, dan `contact`.
1. Buat aplikasi baru untuk mengelola profil dan resume:
   ```bash
   python manage.py startapp profile
   ```
2. Buat aplikasi baru untuk mengelola proyek yang pernah dikerjakan:
   ```bash
    python manage.py startapp projects
    ```
3. Buat aplikasi baru untuk mengelola kontak:
   ```bash
   python manage.py startapp contact
   ```
4. Tambahkan `profile`, `projects`, dan `contact` ke bagian `INSTALLED_APPS` di file `settings.py`.
5. Pindahkan file HTML yang berhubungan dengan profil ke dalam folder `templates/profile` yang ada di app `profile`.
6. Pindahkan file HTML yang berhubungan dengan proyek ke dalam folder `templates/projects` yang ada di app `projects`.
7. Pindahkan file HTML yang berhubungan dengan kontak ke dalam folder `templates/contact` yang ada di app `contact`.
8. Buat file `urls.py` di dalam folder `profile`, `projects`, dan `contact` untuk menangani URL yang berhubungan dengan profil, proyek, dan kontak.

- Contoh file `urls.py` di app `profile`:
  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.profile, name='profile'),
      path('resume/', views.resume, name='resume'),
  ]
  ```
- Contoh file `urls.py` di app `projects`:
  ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.projects, name='projects'),
       path('<int:pk>/', views.project_detail, name='project_detail'),
   ]
   ```
- Contoh file `urls.py` di app `contact`:
- Contoh file `urls.py` di app `contact`:
  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.contact, name='contact'),
      path('response/', views.response, name='response'),
  ]
  ```
9. Perbarui file `urls.py` di folder proyek Django Anda untuk mengarahkan URL ke aplikasi yang sesuai.

- Contoh file `urls.py` di folder proyek Django:
  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('profile.urls')),
      path('projects/', include('projects.urls')),
      path('contact/', include('contact.urls')),
  ]
  ```
10. Perbarui view untuk menampilkan data profil, resume, proyek, dan kontak di masing-masing aplikasi.
11. Hapus aplikasi `webapp` dari folder proyek Django Anda. Jangan lupa untuk menghapus referensi ke aplikasi `webapp` di file `settings.py`.

Tampilan struktur folder aplikasi setelah langkah ini:
```
mywebsite/
├── profile/
│   ├── migrations/
│   ├── templates/
│   │   └── profile/
│   │       ├── profile.html
│   │       └── resume.html
│   ├── tests.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── projects/
│   ├── migrations/
│   ├── templates/
│   │   └── projects/
│   │       ├── projects.html
│   │       └── project_detail.html
│   ├── tests.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── contact/
│   ├── migrations/
│   ├── templates/
│   │   └── contact/
│   │       ├── contact.html
│   │       └── response.html
│   ├── tests.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── mywebsite/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── manage.py
```



### Langkah 2: Membuat base template untuk website Anda.
1. Buat file `base.html` di dalam folder `templates` di folder proyek Django Anda.
2. Pindahkan kode HTML yang berulang di setiap halaman (navbar dan footer) ke dalam file `base.html`.
3. Gunakan tag `{% block %}` dan `{% endblock %}` untuk menandai bagian konten yang berbeda di setiap halaman. Misalkan:
   - `{% block title %}` untuk judul halaman.
   - `{% block content %}` untuk konten halaman.

   
- Contoh isi file `base.html` yang diambilkan dari template web Personal [Start Bootstrap - Personal](https://startbootstrap.com/theme/personal):
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>{% block title %}My Website{% endblock %}</title>
  </head>
  <body>
      <nav>
          <ul>
              <li><a href="/">Home</a></li>
              <li><a href="/profile/">Profile</a></li>
              <li><a href="/projects/">Projects</a></li>
              <li><a href="/contact/">Contact</a></li>
          </ul>
      </nav>
      <main>
          {% block content %}
          {% endblock %}
      </main>
      <footer>
          &copy; 2021 My Website
      </footer>
  </body>
  </html>
  ```
4. Gunakan tag `{% extends %}` untuk menghubungkan file `base.html` dengan file HTML lainnya.
- Contoh isi file `profile.html`:
  ```html
  {% extends 'base.html' %}

  {% block title %}Profile - My Website{% endblock %}

  {% block content %}
  <h1>Profile</h1>
  <p>Ini adalah halaman profil saya.</p>
  {% endblock %}
  ```
Ulangi langkah yang sama untuk file HTML lainnya.

5. Perbarui file HTML lainnya yang ada di semua apps untuk menggunakan file `base.html` sebagai template dasar.
   
Tampilan struktur folder aplikasi setelah langkah ini, **terdapat penaikan file `base.html` di folder `templates`**:
```
mywebsite/
├── profile/
│   ├── migrations/
│   ├── templates/
│   │   └── profile/
│   │       ├── profile.html
│   │       └── resume.html
│   ├── tests.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── projects/
│   ├── migrations/
│   ├── templates/
│   │   └── projects/
│   │       ├── projects.html
│   │       └── project_detail.html
│   ├── tests.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── contact/
│   ├── migrations/
│   ├── templates/
│   │   └── contact/
│   │       ├── contact.html
│   │       └── response.html
│   ├── tests.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── mywebsite/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── templates/
│   └── base.html
└── manage.py
```



### Langkah 3: Membuat model untuk profil, proyek, dan kontak.
1. Buat model untuk profil dan resume di app `profile`.
   - Contoh model untuk profil:
     ```python
     from django.db import models

     class Profile(models.Model):
         name = models.CharField(max_length=100)
         email = models.EmailField()
         phone = models.CharField(max_length=15)
         address = models.TextField()
         about = models.TextField()
         education = models.TextField()
         experience = models.TextField()
         skills = models.TextField()
     ```
   - Contoh model untuk resume:
     ```python
       from django.db import models

         class Resume(models.Model):
            title = models.CharField(max_length=100)
            description = models.TextField()
            start_date = models.DateField()
            end_date = models.DateField()
       ```

2. Buat model untuk proyek di app `projects`.
   - Contoh model untuk proyek:
     ```python
     from django.db import models

     class Project(models.Model):
         title = models.CharField(max_length=100)
         description = models.TextField()
         start_date = models.DateField()
         end_date = models.DateField()
         image = models.ImageField(upload_to='images/')
     ```

3. Buat model untuk kontak di app `contact`.
- Contoh model untuk kontak:
  ```python
  from django.db import models

  class Contact(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      message = models.TextField()
  ```
4. Migrasikan model ke dalam database dengan perintah:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Tambahkan model ke dalam Django Admin untuk memudahkan pengelolaan data.

File `mywebsite/profile/admin.py`:
```python
from django.contrib import admin
from .models import Profile, Resume

admin.site.register(Profile)
admin.site.register(Resume)
```

File `mywebsite/projects/admin.py`:
```python
from django.contrib import admin
from .models import Project

admin.site.register(Project)
```

File `mywebsite/contact/admin.py`:
```python
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
```
6. Tambahkan data profil, proyek, dan kontak ke dalam database melalui Django Admin.
   - Buat superuser baru dengan perintah:
     ```bash
     python manage.py createsuperuser
     ```
   - Akses Django Admin di browser dengan alamat `http://localhost:8000/admin/`.
   - Masuk menggunakan username dan password superuser yang telah dibuat.
   - Tambahkan data profil, proyek, dan kontak melalui Django Admin.
   - Silahkan merujuk ke [Django Tutorial part 2](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#introducing-the-django-admin) untuk cara menambahkan data ke dalam database menggunakan Django Admin.
7. Pastikan data yang Anda tambahkan sudah muncul di halaman Django Admin.

### Langkah 4: Menampilkan data profil, dan resume ke dalam halaman web.
1. Perbarui view untuk menampilkan data profil dan resume di app `profile`.
   - Contoh view untuk profil:
     ```python
     from django.shortcuts import render
     from .models import Profile, Resume

     def profile(request):
         profile = Profile.objects.first()
         return render(request, 'profile/profile.html', {'profile': profile})

     def resume(request):
         resume = Resume.objects.all()
         return render(request, 'profile/resume.html', {'resume': resume})
     ```
2. Perbarui file HTML yang berhubungan dengan profil dan resume yang ada di di folder `profile/templates/profile` untuk menampilkan data dari database.
   - Contoh isi file `profile.html`:
     ```html
     {% extends 'base.html' %}

     {% block title %}Profile - My Website{% endblock %}

     {% block content %}
     <h1>{{ profile.name }}</h1>
     <p>{{ profile.email }}</p>
     <p>{{ profile.phone }}</p>
     <p>{{ profile.address }}</p>
     <p>{{ profile.about }}</p>
     <p>{{ profile.education }}</p>
     <p>{{ profile.experience }}</p>
     <p>{{ profile.skills }}</p>
     {% endblock %}
     ```
   - Contoh isi file `resume.html`:
     ```html
     {% extends 'base.html' %}

     {% block title %}Resume - My Website{% endblock %}

     {% block content %}
       <h1>Resume</h1>
       {% for item in resume %}
         <h2>{{ item.title }}</h2>
         <p>{{ item.description }}</p>
         <p>{{ item.start_date }} - {{ item.end_date }}</p>
       {% endfor %}
       {% endblock %}
       ```
3. Uji coba halaman profil dan resume di browser.
4. Pastikan data profil dan resume muncul dengan benar.
5. Jika ada kesalahan, perbaiki kode Anda dan uji coba kembali
6. Jika sudah benar, lanjutkan ke langkah berikutnya.

### Langkah 5: Menampilkan data proyek ke dalam halaman web.
1. Perbarui view untuk menampilkan data proyek di app `projects`.
   - Contoh view untuk proyek:
     ```python
     from django.shortcuts import render
     from .models import Project

     def projects(request):
         projects = Project.objects.all()
         return render(request, 'projects/projects.html', {'projects': projects})

     def project_detail(request, pk):
         project = Project.objects.get(pk=pk)
         return render(request, 'projects/project_detail.html', {'project': project})
     ```

2. Perbarui file HTML yang berhubungan dengan proyek yang ada di folder `projects/templates/projects` untuk menampilkan data dari database.
   - Contoh isi file `projects.html`:
     ```html
     {% extends 'base.html' %}

     {% block title %}Projects - My Website{% endblock %}

     {% block content %}
       <h1>Projects</h1>
       {% for project in projects %}
         <h2>{{ project.title }}</h2>
         <p>{{ project.description }}</p>
         <p>{{ project.start_date }} - {{ project.end_date }}</p>
         <a href="{% url 'project_detail' project.pk %}">Detail</a>
       {% endfor %}
     {% endblock %}
     ```
3. Uji coba halaman proyek di browser.
4. Pastikan data proyek muncul dengan benar.
5. Jika ada kesalahan, perbaiki kode Anda dan uji coba kembali
6. Jika sudah benar, lanjutkan ke langkah berikutnya.

### Langkah 6: Menambahkan halaman detail untuk setiap proyek.
1. Tambahkan view untuk menampilkan detail proyek di app `projects`.
2. Tambahkan URL untuk menampilkan detail proyek di `urls.py` di app `projects`.
   - Contoh URL untuk detail proyek:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.projects, name='projects'),
         path('<int:pk>/', views.project_detail, name='project_detail'),
     ]
     ```
3. Tambahkan template untuk menampilkan detail proyek di folder `templates/projects`.
4. Perbarui file HTML yang berhubungan dengan detail proyek untuk menampilkan informasi lebih lengkap.
5. Uji coba halaman detail proyek di browser.
6. Pastikan informasi proyek muncul dengan benar.
7. Jika ada kesalahan, perbaiki kode Anda dan uji coba kembali
8. Jika sudah benar, lanjutkan ke langkah berikutnya.

### Langkah 7: Menampilkan data kontak ke dalam halaman web.
1. Buat view untuk menampilkan data kontak di app `contact`.
2. Tambahkan URL untuk menampilkan data kontak di `urls.py` di app `contact`.
3. Tambahkan template untuk menampilkan data kontak di folder `templates/contact`.
4. Perbarui file HTML yang berhubungan dengan kontak untuk menampilkan data dari database.
5. Uji coba halaman kontak di browser.
6. Pastikan data kontak muncul dengan benar.
7. Jika ada kesalahan, perbaiki kode Anda dan uji coba kembali
8. Jika sudah benar, lanjutkan ke langkah berikutnya.

### Langkah 8: Menambahkan halaman response untuk form kontak.
1. Buat view untuk menampilkan halaman response di app `contact`.
2. Tambahkan URL untuk menampilkan halaman response di `urls.py` di app `contact`.
3. Tambahkan template untuk menampilkan halaman response di folder `templates/contact`.
4. Perbarui file HTML yang berhubungan dengan response untuk menampilkan informasi yang dikirim oleh pengunjung.
5. Uji coba halaman response di browser.
6. Pastikan informasi yang dikirim oleh pengunjung muncul dengan benar.
7. Jika ada kesalahan, perbaiki kode Anda dan uji coba kembali
8. Jika sudah benar, selamat! Anda telah menyelesaikan tugas ini.

### Langkah 9: Membuat dokumentasi
1. Buat dokumentasi singkat tentang tugas yang telah Anda selesaikan.
2. Dokumentasi harus mencakup langkah-langkah yang Anda lakukan, perubahan yang Anda buat, dan hasil akhir dari tugas ini.
3. Dokumentasi harus ditulis dalam format Markdown dan disimpan dalam file `README.md` di repository GitHub Anda.
4. Pastikan dokumentasi Anda jelas, rapi, dan mudah dipahami oleh orang lain.
5. Jika ada gambar atau screenshot yang diperlukan, pastikan untuk menyertakannya dalam dokumentasi Anda.

### Langkah 10: Mengirimkan Tugas
1. Setiap langkah yang telah Anda selesaikan harus di-commit ke repository GitHub Anda.
2. Setelah menyelesaikan tugas dan membuat dokumentasi, Anda dapat mengirimkan tugas ini dengan cara membuat `Pull Request` ke repository tugas ini.
3. Tunggu hingga reviewer meninjau tugas Anda dan memberikan umpan balik.
4. Jika ada perubahan atau perbaikan yang diperlukan, lakukan perubahan tersebut dan kirimkan kembali tugas Anda.

Selamat mengerjakan dan semoga sukses! Jika ada pertanyaan atau kendala, jangan ragu untuk bertanya di stream Google Classroom.

