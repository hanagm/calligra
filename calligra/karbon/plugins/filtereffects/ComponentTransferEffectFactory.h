/* This file is part of the KDE project
 * Copyright (c) 2009 Jan Hambrecht <jaham@gmx.net>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; see the file COPYING.LIB.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301, USA.
 */

#ifndef COMPONENTTRANSFEREFFECTFACTORY_H
#define COMPONENTTRANSFEREFFECTFACTORY_H

#include "KoFilterEffectFactoryBase.h"

class KoFilterEffect;

class ComponentTransferEffectFactory : public KoFilterEffectFactoryBase
{
public:
    ComponentTransferEffectFactory();
    virtual KoFilterEffect * createFilterEffect() const;
    virtual KoFilterEffectConfigWidgetBase * createConfigWidget() const;
};

#endif // COMPONENTTRANSFEREFFECTFACTORY_H