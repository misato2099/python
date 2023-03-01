from qgis.core import QgsCategorizedSymbolRenderer, QgsSymbol, QgsRendererCategory
from PyQt5.QtGui import QColor


# read csv file and convert the data to be point layers
kw_pointLayer = ''  # keywords contains in column names for available points data, can be more than one keyword, seperated by ','
kw_pointLayerAttri = ''  # column name for categorizing symbols
# file path of csv file, must add '?delimiter=,' at the end of file name
csvpath = '?delimiter=,'
uri = '{}?type=csv&xField={}&yField={}&crs={}'.format(
    csvpath, 'lon', 'lat', 'EPSG:')  # 4 parameters to be set in format(csv file path, column with longitudinal data, column with latitudinal data, cooridinate system to be used of the layer)
# import file and convert data to be points layer, the data provider must be 'delimitedtext' in csv file
store_all = iface.addVectorLayer(uri, '', 'delimitedtext')


# get the namelist of all attribute of the csv file
colName = []
for field in store_all.fields():
    colName.append(field.name())
    # print(field.name())
# print(colName)
colSelect = []
for i in colName:  # filter specific column names by keywords
    if kw_pointLayer in i:
        colSelect.append(i)
        # print(i)
# print(colSelect)
# filter layer features by namelist
for j in colSelect:
    store_all.setSubsetString(j+" LIKE True")
    # print(f"Name:{i}")
    store_all.getFeatures()
    store_savepath = f'.shp'  # set saving path and file name of filtered point layer
    store_writer = QgsVectorFileWriter.writeAsVectorFormat(
        store_all, store_savepath, "utf-8", driverName="ESRI Shapefile", onlySelected=False)
    store_selected_layer = iface.addVectorLayer(store_savepath, j, 'ogr')
    del(store_writer)
    store_all.setSubsetString("")  # clear filter


# coloring features by category
# select layers by keywords
layers = QgsProject.instance().mapLayers().values()
selected_layers = [layer for layer in layers if any(
    keyword in layer.name().lower() for keyword in [kw_pointLayer])]
# print(selected_layers)
# set category and style for each symbol
for layer in selected_layers:
    # set symbol renderer as categorized
    renderer = QgsCategorizedSymbolRenderer(kw_pointLayerAttri)
    layer.setRenderer(renderer)

    # set symbol style
    symbol1 = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol2 = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol3 = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol4 = QgsSymbol.defaultSymbol(layer.geometryType())

    # set symbol color
    symbol1.setColor(QColor(''))
    symbol2.setColor(QColor(''))
    symbol3.setColor(QColor(''))
    symbol4.setColor(QColor(''))

    # execute changes (values matched with the values in column for categorization, expression of style, symbol name displayed on layer panel)
    cat1 = QgsRendererCategory('value in attribute', symbol1, '')
    cat2 = QgsRendererCategory('value in attribute', symbol2, '')
    cat3 = QgsRendererCategory('value in attribute', symbol3, '')
    cat4 = QgsRendererCategory('value in attribute', symbol4, '')

    # add changes to symbol renderer
    renderer.addCategory(cat1)
    renderer.addCategory(cat2)
    renderer.addCategory(cat3)
    renderer.addCategory(cat4)

    # repaint symbols and update interface
    layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(layer.id())

QgsProject.instance().removeMapLayer(store_all)  # delete original point layers
