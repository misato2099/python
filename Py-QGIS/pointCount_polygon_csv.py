import os
import glob
import csv
import pandas as pd
import processing


# (Optional)Merge layer boundaries for calculation
layer_bases = QgsProject.instance().mapLayersByName(kw_map)
layer_base = layer_bases[0]
dissolve_field = ''  # Field name to dissolve
x = 0

# Perform merge
result = processing.run("native:dissolve", {
    'INPUT': layer_base,
    'FIELD': dissolve_field,
    'OUTPUT': f'{kw_map}_dissolve.shp'
})
dissolved_layer = QgsVectorLayer(
    result['OUTPUT'], f'{kw_map}_dissolved', 'ogr')
QgsProject.instance().addMapLayer(dissolved_layer)
dissolved_layer.setProviderEncoding(u'UTF-8')

# Read the base map layer and loop through to count points in base map layer (polygon)
for i in selected_layers:
    layer_joins = QgsProject.instance().mapLayersByName(
        f'{kw_map}_dissolved')  #  Name of base map layer
    layer_join = layer_joins[0]
    layer_points = QgsProject.instance().mapLayersByName(i.name())  # Name of point layer
    layer_point = layer_points[0]

    field_name = ''  # Grouping field name
    field_index = layer_point.fields().indexOf(field_name)
    if field_index == -1:
        print(f'{field_name} field does not exist in {layer_point.name()}')
        continue

    unique_values = layer_point.uniqueValues(field_index)  # Extract unique values from the field

    for value in unique_values:  # Execute count points in polygon
        join_count = f'{i.name()}_joinCount_{value}.shp'
        selection = layer_point.selectByExpression(
            f'"{field_name}" = \'{value}\'')
        processing.run("native:countpointsinpolygon",
                       {'POLYGONS': layer_join,
                        'POINTS': QgsProcessingFeatureSourceDefinition(layer_point.source(),
                                                                       selectedFeaturesOnly=True,
                                                                       featureLimit=-1,
                                                                       geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),
                        'WEIGHT': '',
                        'CLASSFIELD': '',
                        'FIELD': f'{i.name()[-5:]}_join',
                        'OUTPUT': join_count})

        lyr_join_count = iface.addVectorLayer(join_count, '', 'ogr')  # Add layer to project
        lyr_join_count.setProviderEncoding(u'UTF-8')  # Encode the layer
        
        # Convert the output from floats to integers
        pr = lyr_join_count.dataProvider()
        pr.addAttributes(
            [QgsField(f'{i.name()[-5:]}_{value}', QVariant.Int)])  # Set the new field name and data properties
        lyr_join_count.updateFields()

        exp = QgsExpression(f'to_int("{i.name()[-5:]}_join")')  # QGS expression: Convert to integer
        context = QgsExpressionContext()
        context.appendScopes(
            QgsExpressionContextUtils.globalProjectLayerScopes(lyr_join_count))
        with edit(lyr_join_count):
            for f in lyr_join_count.getFeatures():
                context.setFeature(f)
                f[f'{i.name()[-5:]}_{value}'] = exp.evaluate(context)  # Perform the count
                lyr_join_count.updateFeature(f)
        caps = lyr_join_count.dataProvider().capabilities()
        if caps & QgsVectorDataProvider.DeleteAttributes:
            field_index = lyr_join_count.fields(
            ).indexFromName(f'{i.name()[-5:]}_join')
            res = lyr_join_count.dataProvider().deleteAttributes([field_index])
            lyr_join_count.updateFields()

        print(f'{i.name()[-5:]}_joinCount_{value} calculation completed.')
        x += 1

# Export the results

        file_path = f'{i.name()}_joinCount_{value}.csv'
        encoding = ""  # English: UTF-8 Chinese: cp950
        # Define the delimiter
        delimiter = ","

        # Export all fields
        fields = lyr_join_count.fields()

        # Write to CSV
        with open(file_path, "w", encoding=encoding, newline="") as output_file:

            csv_writer = csv.writer(output_file, delimiter=delimiter)

            # Write header row
            header_row = [field.name() for field in fields]
            csv_writer.writerow(header_row)

            # Write feature values
            for feature in lyr_join_count.getFeatures():
                attribute_values = [feature.attribute(
                    field.name()) for field in fields]
                csv_writer.writerow(attribute_values)
print(f'All calcuations completed, {x} records in total.')
x = 0

# Merge files

files_joined = os.path.join(
    '', '*.csv')

list_files = sorted(glob.glob(files_joined))

df = pd.concat(map(lambda file: pd.read_csv(
    file, encoding=''), list_files), axis=1, ignore_index=False) # encoding=(English: UTF-8 Chinese: cp950)
# Remove duplicated columns
df = df.loc[:, ~mdf.columns.duplicated(keep='first')]
# Saving file
df.to_csv(
    f'{kw_map}_myfilename.csv', index=False, encoding='utf-8-sig')
