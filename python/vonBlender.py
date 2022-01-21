# ***RigUIscript generated by Bone Layers Addon***

import bpy

blm_rig_id = "ovn7zt670hsb"


class BLOP_PT_riguilayers(bpy.types.Panel):
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = 'Item'
	bl_label = "Rig Layers"
	bl_idname = "BLOP_PT_riguilayers"

	@classmethod
	def poll(self, context):
		try:
			return (context.active_object.data.get("blm_rig_id") == blm_rig_id)
		except (AttributeError, KeyError, TypeError):
			return False

	def draw(self, context):
		layout = self.layout
		col = layout.column()


		row = col.row()
		row.prop(context.active_object.data,'layers', index=8, toggle=True, text='ROOT')

		row = col.row()
		row.prop(context.active_object.data,'layers', index=9, toggle=True, text='MAIN')
		row.prop(context.active_object.data,'layers', index=10, toggle=True, text='TWEAK')


class BLOP_PT_customproperties(bpy.types.Panel):
	"""Creates a Rig Properties Panel (Pose Bone Custom Properties)"""
	bl_category = "Rig UI"
	bl_label = "Rig Properties"
	bl_idname = "BLOP_PT_customproperties"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_options = {'DEFAULT_CLOSED'}#

	@classmethod
	def poll(self, context):
		if context.mode != 'POSE':
			return False

		try:
			return (context.active_object.type == 'ARMATURE')
		except (TypeError):
			return False

	def draw(self, context):
		layout = self.layout
		pose_bones = context.active_object.pose.bones
		try:
			selected_bones = [bone.name for bone in context.selected_pose_bones]
			selected_bones += [context.active_pose_bone.name]
		except (AttributeError, TypeError):
			return

		def assign_props(row, val, key):
			row.property = key
			row.data_path = "active_pose_bone"
			try:
				row.value = str(val)
			except:
				pass
		active_pose_bone = context.active_pose_bone

		rna_properties = {
			prop.identifier for prop in bpy.types.PoseBone.bl_rna.properties
			if prop.is_runtime
		}
	# Iterate through selected bones add each prop property of each bone to the panel.

		for bone in context.selected_pose_bones:
			if len(bone.keys()) > 1:
				box = layout.box()
			for key in sorted(bone.keys()):
				if key != '_RNA_UI' and key not in rna_properties:
					val = bone.get(key, "value")
					row = box.row()
					split = row.split(align=True, factor=0.7)
					row = split.row(align=True)
					row.label(text=key, translate=False)
					row = split.row(align=True)
					row.prop(bone, f'["{key}"]', text = "", slider=True)


classes = (BLOP_PT_riguilayers, BLOP_PT_customproperties, )

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
	register()