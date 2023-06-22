from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login
from .forms import UserCreateFrm
from .models import Folder, Files
from .validator import validate_file_type_and_get_object

def user_logout(request):
    '''This function is used for logging-out the user'''
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")

class Login(View):
    '''This class is used for logging user in the application'''
    template = "file_application/html/login.html"
    context = {"title":"Login"}

    def get(self,request):
        context = {}
        context.update(self.context)
        return render(request,self.template,context)

    def post(self,request):
        context = {}
        # getting username and password from request and authenticating user
        context.update(self.context)
        una = request.POST["username"]
        pas = request.POST["password"]
        user = authenticate(username=una, password=pas)
        if user is not None:
            red_url = request.GET.get("next",None)
            if red_url == None:
                red_url = "/"
            login(request,user)
            return redirect(red_url)
        else:
            context["error"]="Invalide crediential."
            return render(request,self.template,context)

class UserCreateView(View):
    '''This class based view is used for creating new user'''
    template = "file_application/html/signup.html"
    
    def get(self,request):
        # creating django form object for displaying form to get input from the user 
        form = UserCreateFrm()
        return render(request,self.template,{"form":form})

    def post(self,request):
        # using django form for validating user crediential and creating new user
        form = UserCreateFrm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return redirect("/")
        else:
            return render(request, self.template, {"title":"Create User",'form': form})

class Home(LoginRequiredMixin, View):
    '''
    This class based view is used for uploading files and also showing home page and searching all files
    '''
    template = "file_application/html/index.html"
    login_url = "/login"

    def get(self,request):
        # get user folder and file details and display it to the page
        search = request.GET.get("search",None)
        folders = Folder.objects.filter(user=request.user, deleted=False)
        if search:
            files = Files.objects.filter(user=request.user, file_name__icontains = search)
        else:
            files = Files.objects.filter(user=request.user, deleted=False, parent_folder=None)
        
        context = {"title":"Home", "folders":folders, "files":files}
        if search:
            context["search"] = search
        return render(request, self.template, context)
    
    def post(self,request):
        '''This method is used for validating multiple files and then uploading it.'''
        # getting parent folder id if there is any
        parent_folder = request.GET.get("parent_folder",None)
        folder = None
        # trying to get parent folder details from db
        if parent_folder != None:
            try:
                folder = Folder.objects.get(id=parent_folder,user=request.user, deleted=False)
            except:
                folder = None

        #getting all files from request object
        req_files = dict(request.FILES)

        # checking if files is present in request files
        if "files" not in req_files:
            return HttpResponse("Please provide file's to upload", status=500)

        # validating file type and getting objects to save into db
        error, objs = validate_file_type_and_get_object(req_files, folder, request.user)
        
        if error != None:
            # sending error code if validation failed
            return HttpResponse(error,status=403)
        
        if len(objs) <= 0:
            # checking if objes are not empty
            return HttpResponse("Files cannot be empty", status=403)

        # saving data to database table in bulk
        Files.objects.bulk_create(objs)

        if folder != None:
            return redirect(f"/folder/{folder.id}")
        else:
            return redirect("/")

class FolderView(LoginRequiredMixin, View):
    '''This Class base view is for handling folder view and displays files related to the folders'''
    template = "file_application/html/index.html"
    login_url = "/login"

    def get(self, request, id):
        '''Getting folder details and its files and then sending response to browser'''
        try:
            folder = Folder.objects.get(id=id,user=request.user, deleted=False)
        except:
            return HttpResponse("Folder does not exist",status = 500)
        files = Files.objects.filter(parent_folder = folder,user=request.user, deleted=False)
        return render(request, self.template, {"title":"Home", "folder_id":id,"folder":folder, "files":files})

class FolderCreateView(LoginRequiredMixin, View):
    '''This Class base view is used for creating new folder'''
    login_url = "/login"

    def post(self,request):
        # this method will help in creating new folder
        try:
            f_name = request.POST["f_name"]
            Folder.objects.create(user = request.user,f_name = f_name)
            return HttpResponse("Successfully created")
        except Exception as e:
            return HttpResponse("Error occured: "+str(e),status=500)
    
class FolderDelete(LoginRequiredMixin, View):
    '''This class based view is used for deleting folder and its related files for a user'''
    def post(self,request):
        try:
            # this method will delete the folder requested by the user
            f_id = request.POST["fld_id"]
            obj = Folder.objects.get(user = request.user, id=f_id, deleted=False)
            #deleting its related file's 
            Files.objects.filter(user = request.user, parent_folder=obj, deleted=False).update(deleted=True)
            obj.deleted = True
            obj.save()
            return HttpResponse("Successfully deleted")

        except Exception as e:
            return HttpResponse("Error occured: {e}",status = 500)

class FileDelete(LoginRequiredMixin, View):
    '''This class based view is used for deleting file for a user'''
    def post(self,request):
        try:
            # This method is used for deleting file
            f_id = request.POST["f_id"]
            obj = Files.objects.get(user = request.user, id=f_id, deleted=False)
            obj.deleted = True
            obj.save()
            return HttpResponse("Successfully deleted")

        except Exception as e:
            return HttpResponse("Error occured: {e}",status = 500)


        
