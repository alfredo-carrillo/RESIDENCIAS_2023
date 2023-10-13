from django.shortcuts import render, get_object_or_404, redirect 

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.urls import reverse

from django.views import generic
from django.views.generic import TemplateView,CreateView, UpdateView
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Question, Choice
from .forms import LoginForm, ChoiceForm, QuestionForm, CreatePollform
from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory

questionFormset = modelformset_factory(
    Question, form = QuestionForm, extra = 1)


ChoiceFormset = modelformset_factory(Choice, form=ChoiceForm, extra=1)


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

class CreatePoll(CreateView):
    form_class =    CreatePollform
    template_name = 'crud/create_poll.html'
    #succes = 'polls-main'

    #def form_valid(self, form):
    #    pregunta = form['question'].save()
    #    opcion = form['choices'].save(commit=False) #se crea una instancia del objeto para que no se guarde de inmediato a la base de datos
    #    opcion2 = form['choices2'].save(commit=False)#  y se deja en espera para si así se requiera se realicen validaciones con los datos 
    #    opcion3 = form['choices3'].save(commit = False)#    antes de ser guardados a la base de datos
    #    opcion.persona = pregunta#  se hace referencia que por cada objeto choices se está relacionando al de questions
    #    opcion2.persona = pregunta## lo que quiere decir que cada opcion pertenece a la pregunta señalada
    #    opcion3.persona = pregunta
    #    opcion.save()       
    #    opcion2.save()
    #    opcion3.save()
    #    return HttpResponseRedirect(reverse('polls:c-pol'))

    def post_new(self, request):

        if request.method == "POST":
            form = CreatePoll(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.question_text = request.POST['question_text']
                post.pub_date = request.POST['pub_date']
                post.choice_text = request.POST['choice_text']
                post.votes = request.POST['votes']
                post.save()
                return redirect(reverse('polls:main'), pk= post.pk)
                #return HttpResponseRedirect(reverse_lazy('success') )
        else:
            form = CreatePoll()
        return render(request, 'crud/create_poll.html', {'form': form})
#
   
        


        
        #if request.method == 'POST':
        #    #Se procesa la informacion del formulario
        #    form = form(data = request.POST)
#
        
                   

            
            

