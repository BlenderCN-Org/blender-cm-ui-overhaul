bl_info = {
    "name": "Color Management UI overhaul",
    "description": "Proposal for Blender's color management UI. Part of my research at the BI on what to improve.",
    "author": "Sam Van Hulle",
    "version": (1, 0, 0),
    "blender": (2, 81, 0),
    "location": "Properties > Render",
    "category": "Render"
}


##############################################################################
# Imports
##############################################################################


import bpy


##############################################################################
# Properties
##############################################################################


class ColorManagementMockupProperties(bpy.types.PropertyGroup):

    ocio_config_path                        : bpy.props.StringProperty(name = "OCIO Configuration", subtype = 'FILE_PATH', default = "/media/data/blender_guest/cmake_release/bin/2.81/datafiles/colormanagement/config.ocio")
    display_type                            : bpy.props.EnumProperty(name = "Display Type", items = [
                                                ("apple_p3", "Apple Display P3", "apple_p3"),
                                                ("aces", "ACES", "aces")
                                            ], options = {'SKIP_SAVE'})
    rendering_space                         : bpy.props.EnumProperty(name = "Rendering Space", items = [
                                                ("acescg", "ACES - ACEScg", "acescg"),
                                                ("rec709", "Rec. 709", "rec709")
                                            ], options = {'SKIP_SAVE'})
    view_transform                          : bpy.props.EnumProperty(name = "View Transform", items = [
                                                ("srgb", "sRGB", "srgb"),
                                                ("filmic", "Filmic", "filmic")
                                            ], options = {'SKIP_SAVE'})
    look                                    : bpy.props.EnumProperty(name = "Look", items = [
                                                ("none", "None", "none"),
                                                ("medium_contrast", "Medium Contrast", "medium_contrast")
                                            ], options = {'SKIP_SAVE'})
    input_8bit                              : bpy.props.EnumProperty(name = "8-bit Display Referred Files", items = [
                                                ("aces_srgb_texture", "Utility - sRGB - Texture", "aces_srgb_texture"),
                                                ("default_srgb_texture", "sRGB", "default_srgb_texture")
                                            ], options = {'SKIP_SAVE'})
    input_16bit                             : bpy.props.EnumProperty(name = "16-bit Display Referred Files", items = [
                                                ("aces_srgb_texture", "Utility - sRGB - Texture", "aces_srgb_texture"),
                                                ("default_srgb_texture", "sRGB", "default_srgb_texture")
                                            ], options = {'SKIP_SAVE'})
    input_log                               : bpy.props.EnumProperty(name = "Log Files", items = [
                                                ("adx10", "Input - ADX - ADX10", "adx10"),
                                                ("filmic", "Filmic Log", "filmic")
                                            ], options = {'SKIP_SAVE'})
    input_float                             : bpy.props.EnumProperty(name = "Float Files", items = [
                                                ("ap0", "ACES - ACES2065-1", "ap0"),
                                                ("rec709", "Rec. 709", "rec709")
                                            ], options = {'SKIP_SAVE'})
    output_space                            : bpy.props.EnumProperty(name = "Output Space", items = [
                                                ("ap0", "ACES - ACES2065-1", "ap0"),
                                                ("rec709", "Rec. 709", "rec709")
                                            ], options = {'SKIP_SAVE'})
    apply_view_transform                    : bpy.props.BoolProperty(name = "Apply View Transform", options = {'SKIP_SAVE'})


##############################################################################
# Panels
##############################################################################


class CM_PT_render_properties(bpy.types.Panel):

    bl_idname = "CM_PT_render_properties"
    bl_label = "Color Management"
    bl_region_type = 'WINDOW'
    bl_space_type = 'PROPERTIES'
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        lay = self.layout
        lay.use_property_split = True
        lay.prop(context.scene.cm_properties, "ocio_config_path")
        lay.prop(context.scene.cm_properties, "display_type")


class CM_PT_transform_preferences(bpy.types.Panel):

    bl_idname = "CM_PT_transform_preferences"
    bl_label = "Transform Preferences"
    bl_region_type = 'WINDOW'
    bl_space_type = 'PROPERTIES'
    bl_context = "render"
    bl_parent_id = "CM_PT_render_properties"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        lay = self.layout
        lay.use_property_split = True
        lay.prop(context.scene.cm_properties, "rendering_space")
        lay.prop(context.scene.cm_properties, "view_transform")
        lay.prop(context.scene.cm_properties, "look")


class CM_PT_input_rules(bpy.types.Panel):

    bl_idname = "CM_PT_input_rules"
    bl_label = "Input Rules"
    bl_region_type = 'WINDOW'
    bl_space_type = 'PROPERTIES'
    bl_context = "render"
    bl_parent_id = "CM_PT_render_properties"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        lay = self.layout
        lay.use_property_split = True
        lay.prop(context.scene.cm_properties, "input_8bit")
        lay.prop(context.scene.cm_properties, "input_16bit")
        lay.prop(context.scene.cm_properties, "input_log")
        lay.prop(context.scene.cm_properties, "input_float")


class CM_PT_output_preferences(bpy.types.Panel):

    bl_idname = "CM_PT_output_preferences"
    bl_label = "Output Preferences"
    bl_region_type = 'WINDOW'
    bl_space_type = 'PROPERTIES'
    bl_context = "render"
    bl_parent_id = "CM_PT_render_properties"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        lay = self.layout
        lay.use_property_split = True
        lay.prop(context.scene.cm_properties, "output_space")
        lay.prop(context.scene.cm_properties, "apply_view_transform")


##############################################################################
# Registration
##############################################################################


classes = [
    ColorManagementMockupProperties,
    CM_PT_render_properties,
    CM_PT_transform_preferences,
    CM_PT_input_rules,
    CM_PT_output_preferences
]


def register():
    for class_to_register in classes:
        bpy.utils.register_class(class_to_register)
    bpy.types.Scene.cm_properties = bpy.props.PointerProperty(type = ColorManagementMockupProperties)


def unregister():
    for class_to_register in classes:
        bpy.utils.unregister_class(class_to_register)
    try:
        del bpy.types.Scene.cm_properties
    except:
        pass


if __name__  ==  "__main__":
    register()
