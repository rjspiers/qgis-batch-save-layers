# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BatchSaveLayers
                                 A QGIS plugin
 Save open vector layers to one directory as shapefile
                             -------------------
        begin                : 2016-02-19
        copyright            : (C) 2016 by Robert Spiers
        email                : rjspiers1@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BatchSaveLayers class from file BatchSaveLayers.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .batch_save_layers import BatchSaveLayers
    return BatchSaveLayers(iface)
