from django import template

register = template.Library()

@register.filter
def get_html_view_for_file_type(f_obj):
    '''This function is used for checking file type and then returns correct html tag'''
    f_type = f_obj.file_name.split(".")[-1]
    if f_type.strip() == "txt":
        return f'<textarea target="_blank" href="/media/{f_obj.file}" style="width:100%;height: 150px;cursor: pointer;"  class="card-img-top" value="" disabled>{f_obj.file.read().decode()}</textarea>'
    return f'<img src="/media/{f_obj.file}" style="width:100%;height: 150px;" class="card-img-top" alt="{f_obj.file_name}">'
