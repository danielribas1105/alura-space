from django.shortcuts import redirect, render
from usuarios.form import LoginForms, CadastroForms

def login(request):
   form = LoginForms()
   return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
   form = CadastroForms()

   if request.method == 'POST':
      form = CadastroForms(request.POST)

   
   if form.is_valid():
      if form["senha_1"].value() != form["senha_2"].value():
         return redirect('cadastro')
      
      nome = form["nome_cadastro"].value()
      email = form["email"].value()
      senha = form["senha_1"].value()


   return render(request, "usuarios/cadastro.html", {"form": form})