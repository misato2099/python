import glob
import os
from qgis.core import QgsCategorizedSymbolRenderer, QgsSymbol, QgsRendererCategory
from PyQt5.QtGui import QColor


# filter keywords of values in attribute
kw = ['%', '%']  # '%' is wildcard
files_joined = os.path.join(
    '', '*.shp')  # input folder path in''
list_files = sorted(glob.glob(files_joined))  # sort files in folder
# print(list_files)
for file in list_files:
    layer = iface.addVectorLayer(
        file, file[-13:-4], 'ogr')  # get all file names
    layer.setProviderEncoding(u'utf-8')  # set coding format of files
    layer.dataProvider().setEncoding(u'utf-8')  # set coding format of files
    layer.setSubsetString("CODE LIKE "+f"'{kw[0]}'"
                          + " OR CODE LIKE "+f"'{kw[1]}'"
                          )  # filter values by keywords
    # add new attribute for categorization
    pr = layer.dataProvider()
    # set attribute name and property(String in this case)
    pr.addAttributes([QgsField('attribute name', QVariant.String)])
    layer.updateFields()
    # calculate the value of new attribute by QGS expression
    conditions = ' '.join([f'WHEN "CODE" LIKE \'{k}\' THEN \'{v}\''
                           for k, v in zip(kw, ['value1', 'value n'...])])
    expression = f'CASE {conditions} END'
    exp = QgsExpression(expression)
    context = QgsExpressionContext()
    context.appendScopes(
        QgsExpressionContextUtils.globalProjectLayerScopes(layer))
    with edit(layer):
        for f in layer.getFeatures():
            context.setFeature(f)
            f['attribute name'] = exp.evaluate(
                context)  # execute QGS expression
            # update the calculation results of attribute table
            layer.updateFeature(f)
    layer.getFeatures()  # get all filtered features
    layer_savepath = f'.shp'  # set saving path and file name of filtered layers
    layer_writer = QgsVectorFileWriter.writeAsVectorFormat(
        layer, layer_savepath, "utf-8", driverName="ESRI Shapefile", onlySelected=False)
    layer_selected_layer = iface.addVectorLayer(
        layer_savepath, '', 'ogr')  # input displayed name in ''
    del(layer_writer)
    layer.setSubsetString("")  # clear filter
    QgsProject.instance().removeMapLayer(layer)  # delete original layers

# coloring symbols by category

# define the keywords you want to search for in layer names
kw_pointLayer = ''  # keywords contains in column names for available points data, can be more than one keyword, seperated by ','
kw_pointLayerAttri = ''  # column name for categorizing symbols

# get a list of all layers in the project that contain one of the keywords in their name
layers = QgsProject.instance().mapLayers().values()
selected_layers = [layer for layer in layers if any(
    keyword in layer.name().lower() for keyword in [kw_pointLayer])]
print(selected_layers)
# iterate over the selected layers and create a categorized symbol renderer for each one
for layer in selected_layers:
    # create a categorized symbol renderer
    renderer = QgsCategorizedSymbolRenderer(kw_pointLayerAttri)
    layer.setRenderer(renderer)

    # create a symbol for each category
    symbol1 = QgsSymbol.defaultSymbol(layer.geometryType())
    # need to set source path if using SVG image
    svgSymbol1 = QgsSvgMarkerSymbolLayer("source path.svg", size=3)
    svgSymbol1.setFillColor(QColor(''))
    symbol1.changeSymbolLayer(0, svgSymbol1)

    symbol2 = QgsSymbol.defaultSymbol(layer.geometryType())
    svgSymbol2 = QgsSvgMarkerSymbolLayer("source path.svg", size=5)
    svgSymbol2.setFillColor(QColor(''))
    symbol2.changeSymbolLayer(0, svgSymbol2)

    # set the symbol of each category (values matched with the values in column for categorization, expression of style, symbol name displayed on layer panel)
    cat1 = QgsRendererCategory('value in attribute', symbol1, '')
    cat2 = QgsRendererCategory('value in attribute', symbol2, '')

    # add the categories to the renderer
    renderer.addCategory(cat1)
    renderer.addCategory(cat2)

    # refresh the layer
    layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(layer.id())
