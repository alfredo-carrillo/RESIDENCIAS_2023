
from django.shortcuts import render, get_object_or_404, redirect 

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy

from .models import Question, Choice
from .forms import LoginForm, CreatePollsForm,  choiceFormset

from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.http import HttpResponseRedirect



class Home(TemplateView):
    template_name = 'polls/home.html'


class MainView(generic.list.ListView):
    model = Question
    template_name = 'polls/index.html'
    
      
    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super(MainView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
      #  print(context)
        return context
    
    def get_object(self):
        return Question.objects.all().order_by('-pub_date')

    
    def get(self, request):
        if  not request.user.is_authenticated:
        # messwages.warning(request, 'MENSAJE: Usuario no logeado')
            return redirect(reverse('polls:register'))
        else:
            
            #import pdb; pdb.set_trace()
            context = self.get_context_data()
            return render(request, self.template_name, context)

class DetailView(generic.DetailView):
    #import pdb; pdb.set_trace()   
    model = Question
    template_name = 'polls/detail.html'


    def get_queryset(self):
        
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte = timezone.now())      
   
def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class ResultView(generic.DetailView):
    model =   Question
    template_name = 'polls/results.html'


##  LOGIN VEW   #######

class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    form = LoginForm()

         
    def get(self, request):
        #import pdb; pdb.set_trace()
        if request.method == 'GET':
            form = LoginForm()
            return render(request, self.template_name, {'form': form}) 
        else:
            messages.warning(request, 'no existe formilario') 

        if request.user.is_authenticated:
            return redirect(reverse('polls:main'))
        else: 
            return render(request, self.template_name)   

    def post(self, request):
        form = LoginForm()
        #import pdb; pdb.set_trace()
        username = request.POST['username']
        password = request.POST['password']

        #import pdb; pdb.set_trace()
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('polls:main')  #  redirigir al usuario después de iniciar sesión.
        else:
            # Handle authentication failure (e.g., show an error message)
            messages.error(request, 'La contraseña o el usuario son incorrectos, verifica los datos')
            form = LoginForm()
            return render(request, self.template_name, {'form': form}) 

def logout_view(request):
    logout(request)#toma el request de la pagina con el url asignado y retornar la peticion
    messages.warning(request, 'MENSAJE: El usuario ha cerrado la sesion')
    #redirigiendo al home
    return redirect(reverse('polls:home'))

##      CRUD VIEWS          #####




class CreatePoll(generic.CreateView):
    model = Question
    template_name = 'crud/create_poll.html'
    form = CreatePollsForm()

    def get(self, request):
        #import pdb; pdb.set_trace()
        if request.method == 'GET':
            form = CreatePollsForm()
            return render(request, self.template_name, {'form': form}) 
        else:
            messages.warning(request, 'no existe formilario') 

        

    def post(self, request):
        form = CreatePollsForm()
        #import pdb; pdb.set_trace()
        question_text = request.POST['question_text']
        pub_date = request.POST['pub_date']
        choice_text = request.POST['choice_text']
        votes = request.POST['votes']

    def form_valid(self, form):
        context = self.get_context_data()
        choice_formset = context['choice_formset']
        if choice_formset.is_valid():
            self.object = form.save()
            choice_formset.instance = self.object
            choice_formset.save()
            return redirect(reverse("polls:main"))
        else:
            messages.error(self.request, 'Error en el formset')
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['choice_formset'] = choiceFormset(self.request.POST, instance=self.object)
        else:
            context['choice_formset'] = choiceFormset(instance=self.object)
        return context

    
    