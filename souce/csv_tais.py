import bpy
import csv

def import_fbx(path_i):
    bpy.ops.import_scene.fbx(filepath=path_i, axis_forward='-Z', axis_up='Y', directory="", filter_glob="*.fbx", ui_tab='MAIN', use_manual_orientation=False, global_scale=1.0, bake_space_transform=False, use_custom_normals=True, use_image_search=True, use_alpha_decals=False, decal_offset=0.0, use_anim=True, anim_offset=1.0, use_custom_props=True, use_custom_props_enum_as_string=True, ignore_leaf_bones=False, force_connect_children=False, automatic_bone_orientation=False, primary_bone_axis='Y', secondary_bone_axis='X', use_prepost_rot=True)
    return

def export_fbx(path_e):
    bpy.ops.export_scene.fbx(filepath=path_e, check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx", version='BIN7400', ui_tab='MAIN', use_selection=False, global_scale=1.0, apply_unit_scale=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LAMP', 'MESH', 'OTHER'}, use_mesh_modifiers=True, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, use_anim=True, use_anim_action_all=True, use_default_take=True, use_anim_optimize=True, anim_optimize_precision=6.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True)
    return

#é¿çsïîï™

with open('C:\\Users\\taisy\\Documents\\GameEngineproject\\basemap\\data\\basemap.csv','r') as f:
    fld = list(csv.reader(f))


path = 'D:\\TBA\\result\\'
#path = '/home/taisyo/TBA/result/'
tail = '.fbx'

#allbase = 'D:\\TBA\\base\\allbase.fbx'

for x in range(100):
    path_i = path + str(x) + tail
    import_fbx(path_i)

data_ = []
mat_ = []
count = 0

for x in bpy.data.objects:
    data_.append(x)

for y in range(10):
    for x in range(10):
        for m in data_[count].material_slots:
            insert_flag = 1
            for m2 in mat_:
                if (m.name[0:5] == m2.name):
                    bpy.data.materials.remove(m.material)
                    m.material = m2
                    insert_flag = 0
                    break
            if (insert_flag == 1):
                mat_.append(m.material)


        data_[count].location.x += x*6
        data_[count].location.y += y*6
        if(fld[y][x]=='0'):
            bpy.data.objects.remove(data_[count])
        count += 1

path_e = path + 'res' + tail
export_fbx(path_e)


