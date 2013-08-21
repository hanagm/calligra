/* This file is part of the KDE project
   Copyright 2008 Stefan Nikolaus <stefan.nikolaus@kdemail.net>

   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Library General Public
   License as published by the Free Software Foundation; either
   version 2 of the License, or (at your option) any later version.

   This library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Library General Public License for more details.

   You should have received a copy of the GNU Library General Public License
   along with this library; see the file COPYING.LIB.  If not, write to
   the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.
*/

#ifndef KSPREAD_ODF_LOADING_CONTEXT
#define KSPREAD_ODF_LOADING_CONTEXT

#include <KoOdfLoadingContext.h>

#include <QHash>

#include "Region.h"

class KoShapeLoadingContext;
class KoShape;

namespace Calligra
{
namespace Sheets
{

/**
 * \ingroup OpenDocument
 * Data used while loading.
 */
class OdfLoadingContext
{
public:
    explicit OdfLoadingContext(KoOdfLoadingContext &odfContext)
            : odfContext(odfContext), shapeContext(0) {}

public:
    KoOdfLoadingContext& odfContext;
    KoShapeLoadingContext* shapeContext;
    QHash<QString, KoXmlElement> validities;
};

struct ShapeLoadingData {
    KoShape* shape;
    QPoint startCell;
    QPointF offset;
    Region endCell;
    QPointF endPoint;
};

} // namespace Sheets
} // namespace Calligra

#endif // KSPREAD_ODF_LOADING_CONTEXT