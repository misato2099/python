# import base map layer and filter specific province
from random import randrange


# filter province
kw_map = ''  # province name
basepath = ''  # vector layer path
# input the layer name to be displayed on layer panel to ''
admin_all = iface.addVectorLayer(basepath, '', 'ogr')
admin_all.setProviderEncoding(u'UTF-8')  # set coding format of soruce layer
# set coding format of soruce layer
admin_all.dataProvider().setEncoding(u'UTF-8')
admin_all.setSubsetString("COUNTYNAME LIKE "+f"'{kw_map}'")  # execute filter
admin_all.getFeatures()  # get filtered features of the layer
admin_savepath = f'.shp'  # saving path of filtered layer
admin_writer = QgsVectorFileWriter.writeAsVectorFormat(
    admin_all, admin_savepath, "utf-8", driverName="ESRI Shapefile", onlySelected=False)  # execute saving
admin_selected_layer = iface.addVectorLayer(
    admin_savepath, kw_map, 'ogr')  # add filtered layer to layer panel
del(admin_writer)
admin_all.setSubsetString("")  # clear filter


# coloring of districts
fni = admin_selected_layer.fields().indexFromName(
    '')  # set column for grouping in ''
# filter the unique values of the selected column
unique_values = admin_selected_layer.uniqueValues(fni)

# extract the namelist of all districts
categories = []
for unique_value in unique_values:
    # initializing the symbol
    symbol = QgsSymbol.defaultSymbol(admin_selected_layer.geometryType())

    # set random unrepeated color for each district by iterate
    layer_style = {}
    layer_style['color'] = '%d, %d, %d' % (
        randrange(0, 256), randrange(0, 256), randrange(0, 256))
    layer_style['outline'] = '#000000'
    symbol_layer = QgsSimpleFillSymbolLayer.create(layer_style)

    # update features
    if symbol_layer is not None:
        symbol.changeSymbolLayer(0, symbol_layer)

    # update symbology of features
    category = QgsRendererCategory(unique_value, symbol, str(unique_value))
    # append symbology to districts
    categories.append(category)

# update symbol renderer from single to categorized according to selected column
renderer = QgsCategorizedSymbolRenderer('', categories)

# execute the update of symbol renderer
if renderer is not None:
    admin_selected_layer.setRenderer(renderer)

# repaint all symbol and update all changes above to the interface
admin_selected_layer.triggerRepaint()
# delete the original base map layer
QgsProject.instance().removeMapLayer(admin_all)
iface.layerTreeView().refreshLayerSymbology(
    admin_selected_layer.id())  # refresh the interface
