/* This file is part of the KDE project
 * Copyright (C) 2007 Thomas Zander <zander@kde.org>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public License
 * along with this library; see the file COPYING.LIB.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301, USA.
 */
#include "Plugin.h"
#include "stencilboxdocker/StencilBoxDocker.h"
//#include "stencilboxdocker/StencilShapeFactory.h"

#include <KoDockRegistry.h>
//#include <KoShapeRegistry.h>

#include <kpluginfactory.h>

K_PLUGIN_FACTORY_WITH_JSON(PluginFactory, "flowdockersplugin.json", registerPlugin<Plugin>();)
//K_EXPORT_PLUGIN(PluginFactory("flowdockersplugin"))

Plugin::Plugin(QObject *parent, const QVariantList&)
    : QObject(parent)
{
    Q_UNUSED(parent);
    KoDockRegistry::instance()->add(new StencilBoxDockerFactory());

    //KoShapeRegistry::instance()->add(new StencilShapeFactory());
}
#include "Plugin.moc"