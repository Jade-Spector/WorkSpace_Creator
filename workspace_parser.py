""" Handles the create of the workspace directory"""
import os

def three_proj(p_name,type_sel):
    ''' Confirms if the user wants to create an animation or a static model
    '''

    if type_sel == 'Animated':
        model_folder = 'model'
        textures_folder = 'textures'
        animations_folder = 'animations'
        ref_folder   = 'reference'
        render_folder   = 'renders'
        trender_folder = 'test_renders'
        frender_folder = 'final_renders'
        main_file_path = p_name + '/'
        render_filpath_t = render_folder + '/' + trender_folder
        rrender_filpath_f = render_folder + '/' + frender_folder
        os.makedirs(main_file_path + model_folder)
        os.makedirs(main_file_path + textures_folder)
        os.makedirs(main_file_path + animations_folder)
        os.makedirs(main_file_path + render_folder)
        os.makedirs(main_file_path + ref_folder)
        os.makedirs(main_file_path + render_filpath_t)
        os.makedirs(main_file_path + rrender_filpath_f)
        print("Project Structure Has Been Created.")
    elif type_sel == 'Static':
        model_folder = 'model'
        textures_folder = 'textures'
        ref_folder   = 'reference'
        render_folder   = 'renders'
        trender_folder = 'test_renders'
        frender_folder = 'final_renders'
        main_file_path = p_name + '/'
        render_filpath_t = render_folder + '/' + trender_folder
        rrender_filpath_f = render_folder + '/' + frender_folder
        os.makedirs(main_file_path + model_folder)
        os.makedirs(main_file_path + textures_folder)
        os.makedirs(main_file_path + render_folder)
        os.makedirs(main_file_path + ref_folder)
        os.makedirs(main_file_path + render_filpath_t)
        os.makedirs(main_file_path + rrender_filpath_f)
        print("Project Structure Has Been Created.")

def twod_proj(p_name,type_sel):
    ''' Confirms if the user wants to create an animation or a drawing
    '''
    if type_sel == 'Animated':
        model_folder = 'model_sheets'
        line_test_folder = 'line_tests'
        animations_folder = 'animations'
        ref_folder   = 'reference'
        render_folder   = 'renders'
        main_file_path = p_name + '/'
        os.makedirs(main_file_path + model_folder)
        os.makedirs(main_file_path + line_test_folder)
        os.makedirs(main_file_path + animations_folder)
        os.makedirs(main_file_path + render_folder)
        os.makedirs(main_file_path + ref_folder)

        print("Project Workspace Has Been Created.\n")
    elif type_sel == 'Static':
        drawings_folder = 'drawings'
        ref_folder   = 'reference'
        render_folder   = 'renders'
        main_file_path = p_name + '/'
        os.makedirs(main_file_path + drawings_folder)
        os.makedirs(main_file_path + render_folder)
        os.makedirs(main_file_path + ref_folder)
        print("Project Structure Has Been Created.")

def folder_status(p_name,dem_sel,type_sel):
    ''' Determines what type of folder dir to create.
    '''
    if dem_sel == "2D":
        twod_proj(p_name, type_sel)
    elif dem_sel == "3D":
        three_proj(p_name, type_sel)

def check_name(p_name,dem_sel,type_sel):
    ''' This function will check if a folder of the same name already exists'''
    invalid_name = "";
    try:
        if not os.path.isdir(p_name):
            os.makedirs(p_name)
            folder_status(p_name,dem_sel,type_sel)
            return "created"
        elif p_name == invalid_name:
            raise NotADirectoryError
        else:
            raise FileExistsError
    except FileExistsError:
        print('Folder Already Exists.')
        return"exists"
    except FileExistsError:
        print('Folder Already Exists.')
        return"exists"
def fc_start(p_name,dem_sel,type_sel):
    """ jade-spector: Takes information from the GUI and determines if a 3D or 2D
    project is being created.
    """

    return check_name(p_name,dem_sel,type_sel)
