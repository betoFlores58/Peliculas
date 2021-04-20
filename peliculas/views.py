from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView,TemplateView, FormView
from .models import Post, Productora
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.contrib import messages
from .forms import ContactoForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse, request
from peliculas.forms import ResetPasswordForm

#NO SE USA
def index(request):
    return render(request,'user/index.html')

#No se usa
def catalogo(request):
    peliculas = Post.objects.all()
    data={
        'peliculas': Post
    }
    return render(request,'catalogo.html')

#DEFINICION DEL FROM DE CONTACTO Y REDIRECCIONAMIENTO CON MENSAJE
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
            messages.success(request,"Mensaje enviado correctamente")
            return redirect(to="home")
        else:
            data["form"] = formulario
            
    return render(request,'contacto.html',data)

#Registro para crear nuevo usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Usuario registrado correctamente")
            return redirect(to="home")
        data["form"]=formulario
    return render(request,'registration/registro.html',data)

#DECLARACION DE CLASES TEMPLATES ASIGNANDO EL MODELO Y TEMPLATE CORRESPONDIENTE
class HomeListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'Peliculas'

class CatalogoTemplateView(TemplateView):
    model = Post
    template_name = 'catalogo.html'
    context_object_name = 'Peliculas'

class peliculaView(DetailView):
    model = Post
    template_name = 'pelicula.html'
    context_object_name = 'Peliculas'

class peliculaCreateView(CreateView):
    model = Post
    template_name = "agregarPelicula.html"
    fields = '__all__'
    success_url = reverse_lazy('home')

class peliculaUpdateView(UpdateView):
    model = Post
    template_name = "editarPelicula.html"
    fields = ['nombre','año','descripcion','imagen']
    success_url = reverse_lazy('home')

class peliculaDeleteView(DeleteView):
    model = Post
    template_name = 'eliminarPelicula.html'
    context_object_name = 'Peliculas'
    success_url = reverse_lazy('home')


#Cambiar contraseña de un usuario
class UserChangePasswordView(LoginRequiredMixin, FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('login') 

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = PasswordChangeForm(user=request.user,data=request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data ['error'] = str(e)
        return JsonResponse(data)

#INTENTO DE RESETEO DE PASSWORD (NO SE USA)
class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'registration/resetpwd.html'
    success_url = reverse_lazy('change_password') 

    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        pass
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rseteo de contraseña'
        return context