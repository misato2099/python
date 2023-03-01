from qgis.core import QgsGraduatedSymbolRenderer, QgsRendererRange, QgsColorRampShader, QgsVectorLayerUtils, QgsCategorizedSymbolRenderer, QgsSymbol, QgsRendererCategory
from PyQt5.QtGui import QColor
from qgis.PyQt.QtCore import QVariant


# filter province
kw_map = ''  # province name
basepath = ''  # vector layer path
# input the layer name to be displayed on layer panel to ''
admin_all = iface.addVectorLayer(basepath, '', 'ogr')
admin_all.setProviderEncoding(u'UTF-8')  # set coding format of soruce layer
# set coding format of soruce layer
admin_all.dataProvider().setEncoding(u'UTF-8')
admin_all.setSubsetString("Column name LIKE "+f"'{kw_map}'")  # execute filter
admin_all.getFeatures()  # get filtered features of the layer
admin_savepath = f'.shp'  # saving path of filtered layer
admin_writer = QgsVectorFileWriter.writeAsVectorFormat(
    admin_all, admin_savepath, "utf-8", driverName="ESRI Shapefile", onlySelected=False)  # execute saving
admin_selected_layer = iface.addVectorLayer(
    admin_savepath, kw_map, 'ogr')  # add filtered layer to layer panel
del(admin_writer)
admin_all.setSubsetString("")  # clear filter


# create new atrribute for join table
pr = admin_selected_layer.dataProvider()
# set attribute name and property(String in this case)
pr.addAttributes([QgsField('', QVariant.String)])
admin_selected_layer.updateFields()
# calculate the value of new attribute by QGS expression
exp = QgsExpression('')  # input QGS expression to be executed
context = QgsExpressionContext()
context.appendScopes(
    QgsExpressionContextUtils.globalProjectLayerScopes(admin_selected_layer))
with edit(admin_selected_layer):
    for f in admin_selected_layer.getFeatures():
        context.setFeature(f)
        f[''] = exp.evaluate(context)  # execute QGS expression
        # update the calculation results of attribute table
        admin_selected_layer.updateFeature(f)


# join data setting
joinpath = ''  # source path of data
# import file and set display name, the data provider must be 'delimitedtext' in csv file
pop_all = iface.addVectorLayer(joinpath, '', 'delimitedtext')
pop_all.setProviderEncoding(u'UTF-8')  # set coding format of files
pop_all.dataProvider().setEncoding(u'UTF-8')  # set coding format of files


# join data to target layer
joinField = ''  # set the column name of join table
targetField = ''  # set the column name table being joined
joinLayer = QgsVectorLayerJoinInfo()
joinLayer.setJoinFieldName(joinField)  # set the column name of join table
# set the column name table being joined
joinLayer.setTargetFieldName(targetField)
joinLayer.setJoinLayerId(pop_all.id())
joinLayer.setUsingMemoryCache(True)
joinLayer.setJoinLayer(pop_all)
joinLayer.setPrefix('')  # (optional)delete prefix of joined column names
admin_selected_layer.addJoin(joinLayer)


# get the namelist of all attribute of the csv file
colName = []
for field in admin_selected_layer.fields():
    colName.append(field.name())
    # print(field.name())
# print(colName)
colSelect = []
for i in colName:  # filter specific column names by keywords
    if "" in i:
        colSelect.append(i)
        # print(i)
# print(colSelect)
input_layer = QgsProject.instance().mapLayersByName(kw)[0]

# clone layers and change name according to namelist
for name in colSelect:
    # Make a clone of the input layer
    new_layer = input_layer.clone()
    # Set the new layer name
    new_layer.setName(name)
    # update interface
    QgsProject.instance().addMapLayer(new_layer)


# coloring feature in gradual form
keywords = ['']  # column for categorizing features

# get a list of all layers in the project that contain one of the keywords in their name
layers = QgsProject.instance().mapLayers().values()  # get namelist of all layers
selected_layers = [layer for layer in layers if any(keyword in layer.name(
).lower() for keyword in keywords)]  # select layers by keyword

# iterate over the selected layers and create a categorized symbol renderer for each one
for layer in selected_layers:
    # set up the color ramp with a range :
    color1 = QColor(158, 202, 225)
    color2 = QColor(107, 174, 214)
    color3 = QColor(66, 146, 198)
    color4 = QColor(33, 113, 181)
    color5 = QColor(8, 81, 156)
    color_ramp = QgsGradientColorRamp(color1, color5)

    # set symbol style
    graduated_renderer = QgsGraduatedSymbolRenderer(
        layer.name())  # set symbol renderer(gradual)
    graduated_renderer.setSourceColorRamp(color_ramp)  # set color ramp
    # set attribute for categorization
    graduated_renderer.setClassAttribute(layer.name())
    # set categorization method(use Jenks in this case)
    graduated_renderer.setMode(QgsGraduatedSymbolRenderer.Jenks)
    # execute categorization by method set above
    graduated_renderer.updateClasses(
        layer, QgsGraduatedSymbolRenderer.Jenks, 5)

    # execute changes
    layer.setRenderer(graduated_renderer)

    # update interface
    layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(layer.id())

QgsProject.instance().removeMapLayer(admin_all)  # delete original layer
