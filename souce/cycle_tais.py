import bpy
import random


def join_object():
    for ob in bpy.context.scene.objects:
        #オブジェクトはメッシュか？
        if ob.type == 'MESH':
            ob.select = True
            bpy.context.scene.objects.active = ob
        else :
            ob.select = False

    bpy.ops.object.join()
    return


def import_fbx(path_i):
    bpy.ops.import_scene.fbx(filepath=path_i, axis_forward='-Z', axis_up='Y', directory="", filter_glob="*.fbx", ui_tab='MAIN', use_manual_orientation=False, global_scale=1.0, bake_space_transform=False, use_custom_normals=True, use_image_search=True, use_alpha_decals=False, decal_offset=0.0, use_anim=True, anim_offset=1.0, use_custom_props=True, use_custom_props_enum_as_string=True, ignore_leaf_bones=False, force_connect_children=False, automatic_bone_orientation=False, primary_bone_axis='Y', secondary_bone_axis='X', use_prepost_rot=True)
    return

def export_fbx(path_e):
    bpy.ops.export_scene.fbx(filepath=path_e, check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx", version='BIN7400', ui_tab='MAIN', use_selection=False, global_scale=1.0, apply_unit_scale=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LAMP', 'MESH', 'OTHER'}, use_mesh_modifiers=True, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, use_anim=True, use_anim_action_all=True, use_default_take=True, use_anim_optimize=True, anim_optimize_precision=6.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True)
    return

def refresh_obj():
    for x in bpy.data.objects:
        bpy.data.objects.remove(x)
    #シーン内のオブジェクトを全て消去

        
def refresh_mat():
    for x in bpy.data.materials:
        bpy.data.materials.remove(x)
    #シーン内のマテリアルを全て消去(リフレッシュ)

def refresh_tex():
    for x in bpy.data.textures:
        bpy.data.textures.remove(x)

def refresh():
    refresh_obj()
    refresh_mat()
    refresh_tex()
    #全部リフレッシュ

def rename():
    for x in bpy.data.objects:
        x.name = 'obj'
    #シーン内のオブジェクトの名前を'obj'に統一

def name_mat():
    count = 0;
    for x in bpy.data.materials:
        if (len(x.texture_slots)!=0):
            x.name = bpy.data.textures[x.texture_slots[0].texture.name].image.filepath[-9:-4]



path = 'D:\\TBA\\main\\test.fbx'


#実行部分

refresh()
path_m = 'D:\\TBA\\main\\'
#path_m = '/home/taisyo/TBA/main/'
path_r = 'D:\\TBA\\roof\\'
#path_r = '/home/taisyo/TBA/roof/'
path_p1 = 'D:\\TBA\\parts_1\\'
#path_p1 = '/home/taisyo/TBA/parts_1/'
path_p2 = 'D:\\TBA\\parts_2\\'
#path_p2 = '/home/taisyo/TBA/parts_2/'
tail = '.fbx'
for x in range(20):
    path_mr = path_m + str(random.randint(0,3)) + tail
    path_rr = path_r + str(random.randint(0,5)) + tail
    path_p1r = path_p1 + str(random.randint(0,1)) + tail
    path_p2r = path_p2 + str(random.randint(0,5)) + tail

    import_fbx(path_mr)
    import_fbx(path_rr)
    import_fbx(path_p1r)
    import_fbx(path_p2r)
    
    path_e = 'D:\\TBA\\result\\'+str(x)+'.fbx'
    #path_e = '/home/taisyo/TBA/result/' + str(x) + '.fbx'
    join_object()
    rename()
    name_mat()
    export_fbx(path_e)
    refresh()




