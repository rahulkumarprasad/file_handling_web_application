from django.conf import settings
from .models import Files
from django.views.static import serve
from django.shortcuts import HttpResponse

def validate_file_type_and_get_object(files, folder, user):
    '''This function is used for validating file type and then creating object for file model which will be saved later'''
    supporting_type = ["txt","jpg","jpeg","png"]
    error = None
    list_of_objs = []
    
    if files:
        for file in files["files"]:
                
            f_type = file.name.split(".")[-1]
            if f_type not in supporting_type:
                error = f"file {file.name} is not supported please make sure you are uploading file of type's :{', '.join(supporting_type)}"
                break

            temp_obj = Files(user = user, parent_folder = folder, file_name = file.name, file = file)
            list_of_objs.append(temp_obj)

    return error, list_of_objs

def media_authentication_check(request, path, document_root=None, show_indexes=False):
    '''This function is used for serving media files of the current user by checking the username
    and preventing current user to access files for other user'''
    path_spl = path.split("/")
    usr = request.user
    if path_spl[0].strip() != usr.username or len(path_spl) == 0:
        return HttpResponse("File not found", status=404)
    return serve(request, path, document_root, show_indexes)