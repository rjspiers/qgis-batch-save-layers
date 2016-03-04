# Batch Save Layers

A QGIS plugin to save all open vector layers to a directory.

## Features
A simple GUI dialog in QGIS to:
- Set export directory
- Set file types to write by checklist
- Save all open vector layers at once
- Vector files exported to a directory with the structure of:

```
├── export-directory
│   	├──CSV
│   	├──ESRI Shapefile
│   	├──GeoJSON
│   	├──KML
│   	├──MapInfo File
│   	├──PGDump
```

## Icon
![image of icon](https://raw.githubusercontent.com/rjspiers/qgis-batch-save-layers/master/icon.png)

## GUI Dialog 
![image of GUI](https://raw.githubusercontent.com/rjspiers/qgis-batch-save-layers/gh-pages/batch-save-layers-dialog.png)

##Planned
- Write metadata file to export-directory
- Option to zip
- Specify layers to export
