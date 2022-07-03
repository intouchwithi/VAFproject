from VAFpackage import FunctionalStructure, FS_7_TYPES, FS_4_TYPES
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})

"""4 and 6 element functional structure creation"""
fs_map_4_element = FunctionalStructure(FS_4_TYPES)
fs_map_4_element.write_map_to_file("output/FunctionalStructure/Modern 4 element FS.grd")
figure = fs_map_4_element.get_relative_area_plot()
plt.show()
figure.savefig('output/FunctionalStructure/Modern 4 element FS barplot.jpeg',dpi=1200,bbox_inches='tight')


fs_map_7_element = FunctionalStructure(FS_7_TYPES)
fs_map_7_element.write_map_to_file("output/FunctionalStructure/Modern 7 element FS.grd")
figure2 = fs_map_7_element.get_relative_area_plot()
plt.show()
figure2.savefig('output/FunctionalStructure/Modern 7 element FS barplot.jpeg',dpi=1200,bbox_inches='tight')

