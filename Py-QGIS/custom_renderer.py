# Color and display missing values
from qgis.core import QgsGraduatedSymbolRenderer, QgsRendererRange, QgsColorRampShader, QgsVectorLayerUtils, QgsCategorizedSymbolRenderer, QgsSymbol, QgsRendererCategory
from PyQt5.QtGui import QColor
from qgis.PyQt.QtCore import QVariant


# Load the base map

kw_map = ""  # keyword of base map
basepath = ".shp"  # base map location and file name
admin_all = iface.addVectorLayer(basepath, 'customized base map name', 'ogr')
admin_all.setProviderEncoding(u'UTF-8')  # Encoding to prevent garbled characters
admin_all.dataProvider().setEncoding(u'UTF-8')  # Encoding to prevent garbled characters
admin_all.setSubsetString("COUNTYNAME LIKE "+f"'{kw_map}'")
admin_all.getFeatures()  # Select the filtered features
# Saving path and file name
admin_savepath = f'{kw_map}.shp'
admin_writer = QgsVectorFileWriter.writeAsVectorFormat(
    admin_all, admin_savepath, "utf-8", driverName="ESRI Shapefile", onlySelected=False)
admin_selected_layer = iface.addVectorLayer(
    admin_savepath, kw_map, 'ogr')  # Set the filtered layer as a variable
del(admin_writer)
admin_all.setSubsetString("")


# Merge data
pr = admin_selected_layer.dataProvider()
pr.addAttributes([QgsField('field name to be merged of base map', QVariant.String)])  # Set the column and data attributes (string attribute)
admin_selected_layer.updateFields()
# Output new column values using QGS expressions
exp = QgsExpression('')  # Set the QGS expression to be executed
context = QgsExpressionContext()  # Execute the expression
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(
    admin_selected_layer))  #  () is the variable name of the filtered layer
with edit(admin_selected_layer):
    for f in admin_selected_layer.getFeatures():
        context.setFeature(f)
        f['field name to be merged of base map'] = exp.evaluate(context)  # Execute the calculation
        admin_selected_layer.updateFeature(f)  # Update the field


# Add the data to be inserted into the layer
joinpath = 'file:///.csv'
# Load the layer: Set the file path, customize the layer display name, and set the file format to delimitedtext
pop_all = iface.addVectorLayer(joinpath, 'customized base map name', 'delimitedtext')
pop_all.setProviderEncoding(u'UTF-8')  # Encoding to prevent garbled characters
pop_all.dataProvider().setEncoding(u'UTF-8')  # Encoding to prevent garbled characters


# Insert CSV data into the base layer
joinField = 'field name to be merged of base map and / or csv file data'  # Set the field name to be merged between the base map and CSV file data. If the fields in the joinLayer and targetLayer are different, set them separately
joinLayer = QgsVectorLayerJoinInfo()
joinLayer.setJoinFieldName(joinField)  # Insert data
joinLayer.setTargetFieldName(joinField)  # Insert target layer
joinLayer.setJoinLayerId(pop_all.id())
joinLayer.setUsingMemoryCache(True)
joinLayer.setJoinLayer(pop_all)
joinLayer.setPrefix('')  # (Optional) Delete the prefix of the merge field name
admin_selected_layer.addJoin(joinLayer)


# Group output layers by year
colName = []
for field in admin_selected_layer.fields():  # Returns the name of all attribute fields
    colName.append(field.name())  # Add all field names to a list
    # print(field.name())
# print(colName)
colSelect = []
for i in colName:  # Filter specified fields
    if "keyword of layer name" in i:  # Set the keyword of the output layer field
        colSelect.append(i)
        # print(i)
# print(colSelect)
input_layer = QgsProject.instance().mapLayersByName(kw_map)[0]

# Copy the corresponding number of layers and rename them according to the filter list
for name in colSelect:
    # Make a clone of the input layer
    new_layer = input_layer.clone()  # Copy the corresponding number of layers
    # Set the new layer name
    new_layer.setName(name)  # Name the layer according to the feature field
    # Add to the layer list
    QgsProject.instance().addMapLayer(new_layer)


# Coloring (gradient coloring)
keywords = ['keyword of layer name']  # More sets of keywords can be added after the comma

# Get all layer names and then filter the used layers
layers = QgsProject.instance().mapLayers().values()  # Set the layer variable
selected_layers = [layer for layer in layers if any(
    keyword in layer.name().lower() for keyword in keywords)]  # Filter layers that meet the criteria

# Execute the following command in a loop for the filtered layers
for layer in selected_layers:
    # Create a custom classification list
    myRangeList = []

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())  # Basic feature style (use defaultSymbol for polygon features)
    symbol.setColor(QColor("#f7fbff"))  # Set the color
    # Set the value range (floating point values must have the display text in quotes)
    myRange = QgsRendererRange(0.1, 1000.0, symbol, '1 - 1000')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor("#deebf7"))
    myRange = QgsRendererRange(1000.1, 2000.0, symbol, '1001 - 2000')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor("#c6dbef"))
    myRange = QgsRendererRange(2000.1, 3000.0, symbol, '2001 - 3000')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor("#9ecae1"))
    myRange = QgsRendererRange(3000.1, 4000.0, symbol, '3001 - 4000')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor("#6baed6"))
    myRange = QgsRendererRange(4000.1, 5000.0, symbol, '4001 - 5000')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor("#4292c6"))
    myRange = QgsRendererRange(5000.1, 6000.0, symbol, '5001 - 6000')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor("#2171b5"))
    myRange = QgsRendererRange(6000.1, 7000.0, symbol, '6001 - 7000')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor("#08519c"))
    myRange = QgsRendererRange(7000.1, 8000.0, symbol, '7001 - 8000')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor("#08306b"))
    myRange = QgsRendererRange(8000.1, 9000.0, symbol, '8001 - 9000')
    myRangeList.append(myRange)

    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor("#808080"))
    myRange = QgsRendererRange(-99, 0, symbol, 'No Data')  # The range of missing values is generally -99 to 0
    myRangeList.append(myRange)

    # Set feature grouping method (gradient)
    graduated_renderer = QgsGraduatedSymbolRenderer(
        layer.name(), myRangeList)  # Set layer symbol classification method (gradient)
    graduated_renderer.setMode(
        QgsGraduatedSymbolRenderer.Custom)  # ** Set gradient (custom) classification mode **

    # Perform grouping settings
    layer.setRenderer(graduated_renderer)

    # 更Update the interface
    layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(layer.id())

QgsProject.instance().removeMapLayer(admin_all)  # Delete the original layer
