# get the layer tree root
root = QgsProject.instance().layerTreeRoot()

# iterate through the layers in the root
x = 0  # calculate the numbers of layout have been exported
for i in selected_layers:
    layer_names = [kw_map, i.name()]  # List of layer names to display
    for layer in root.children():
        if layer.name() in layer_names:
            # show the layer
            layer.setItemVisibilityChecked(True)
        else:
            # hide the layer
            layer.setItemVisibilityChecked(False)

    # refresh the map canvas
    canvas = iface.mapCanvas()
    canvas.refreshAllLayers()

    layer_bases = QgsProject.instance().mapLayersByName(kw_map)
    layer_base = layer_bases[0]

    layer_points = QgsProject.instance().mapLayersByName(i.name())
    layer_point = layer_points[0]

    project = QgsProject.instance()
    manager = project.layoutManager()
    layoutName = f"{kw_map}_{i.name()[-5:]}"
    layouts_list = manager.printLayouts()
    # remove any duplicate layouts
    for layout in layouts_list:
        if layout.name() == layoutName:
            manager.removeLayout(layout)
    layout = QgsPrintLayout(project)
    layout.initializeDefaults()
    layout.setName(layoutName)
    manager.addLayout(layout)

    # create map item in the layout
    map = QgsLayoutItemMap(layout)
    map.setRect(20, 20, 20, 20)

    # set the map extent
    ms = QgsMapSettings()
    ms.setLayers([layer_base, layer_point])  # set layers to be mapped
    # set coordinate values(float) according to the coordinate system used
    xmin = float
    ymin = float
    xmax = float
    ymax = float
    rect = QgsRectangle(xmin, ymin, xmax, ymax)
    # set scale of layer displayed, higher value with smaller proportion
    rect.scale(1.0)
    ms.setExtent(rect)
    map.setExtent(rect)
    map.setBackgroundColor(QColor(255, 255, 255, 0))
    layout.addLayoutItem(map)  # add this map into the layout

    # set the placing location of map (left, top)
    map.attemptMove(QgsLayoutPoint(5, 20, QgsUnitTypes.LayoutMillimeters))
    # resize the map wrap (length, width)
    map.attemptResize(QgsLayoutSize(180, 180, QgsUnitTypes.LayoutMillimeters))

    # set legend
    legend1 = QgsLayoutItemLegend(layout)
    legend1.setTitle("")
    # (optional) set whether the legend wrap can be splitted
    legend1.setSplitLayer(False)
    # setSplitLayer must be True before executing setColumnCount
    legend1.setColumnCount(2)
    # set legend font style and size (title), Microsoft JhengHei is used in this case
    legend1.setStyleFont(QgsLegendStyle.Title, QFont('Microsoft JhengHei', 18))
    # set legend font style and size (subgroup)
    legend1.setStyleFont(QgsLegendStyle.Subgroup,
                         QFont('Microsoft JhengHei', 14))
    legend1.setStyleFont(QgsLegendStyle.SymbolLabel, QFont(
        'Microsoft JhengHei', 11))  # set legend font style and size (items)
    layerTree1 = QgsLayerTree()
    # layer displayed in this legend, can add more than one layer
    layerTree1.addLayer(layer_base)
    legend1.model().setRootGroup(layerTree1)
    layout.addLayoutItem(legend1)  # add this legend into the layout
    # set the placing location of legend (left, top)
    legend1.attemptMove(QgsLayoutPoint(
        210, 60, QgsUnitTypes.LayoutMillimeters))

    # (optional) set more than one set of legend
    legend2 = QgsLayoutItemLegend(layout)
    legend2.setTitle("")
    legend2.setSplitLayer(False)
    legend2.setColumnCount(2)
    legend2.setStyleFont(QgsLegendStyle.Title, QFont('Microsoft JhengHei', 18))
    legend2.setStyleFont(QgsLegendStyle.Subgroup,
                         QFont('Microsoft JhengHei', 14))
    legend2.setStyleFont(QgsLegendStyle.SymbolLabel,
                         QFont('Microsoft JhengHei', 11))
    layerTree2 = QgsLayerTree()
    layerTree2.addLayer(layer_point)
    legend2.model().setRootGroup(layerTree2)
    layout.addLayoutItem(legend2)
    legend2.attemptMove(QgsLayoutPoint(
        177, 112.3, QgsUnitTypes.LayoutMillimeters))

    # set scale bar
    scalebar = QgsLayoutItemScaleBar(layout)
    scalebar.setStyle('Line Ticks Up')
    scalebar.setUnits(QgsUnitTypes.DistanceKilometers)
    scalebar.setNumberOfSegments(5)
    scalebar.setNumberOfSegmentsLeft(0)
    scalebar.setUnitsPerSegment(5)
    scalebar.setLinkedMap(map)
    scalebar.setUnitLabel('km')
    scalebar.setFont(QFont('Microsoft JhengHei', 14))
    scalebar.update()
    layout.addLayoutItem(scalebar)
    scalebar.attemptMove(QgsLayoutPoint(
        180, 163, QgsUnitTypes.LayoutMillimeters))

    # set title displayed on layout
    title = QgsLayoutItemLabel(layout)
    title.setText(f"")  # set the word displayed
    title.setFont(QFont('Microsoft JhengHei', 24))
    title.adjustSizeToText()  # auto adjust the wrap of text to fit text size
    # set the position of the title item to be centered
    titleWidth = title.boundingRect().width()
    layoutWidth = layout.pageCollection().page(0).pageSize().width()
    titleX = (layoutWidth - titleWidth) / 2
    titleY = 5  # adjust as needed
    titlePos = QgsLayoutPoint(titleX, titleY, QgsUnitTypes.LayoutMillimeters)
    title.attemptMove(titlePos)
    layout.addLayoutItem(title)

    # export the layout
    layout = manager.layoutByName(layoutName)
    exporter = QgsLayoutExporter(layout)

    # set export path, file name and format of exported layout
    fn = f'.png(or .jpg, .pdf, etc.)'
    # export to image(.png, .jpg, etc.)
    exporter.exportToImage(fn, QgsLayoutExporter.ImageExportSettings())
    # exporter.exportToPdf(fn, QgsLayoutExporter.PdfExportSettings()) # export to pdf file
    x += 1

print(f"{x} layouts have been exported.")
x = 0  # reset the calculation of exported layouts
