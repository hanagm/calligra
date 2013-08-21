/*
 *
 *  Copyright (c) 2007 Adrian Page <adrian@pagenet.plus.com>
 *  Copyright (c) 2008 Tom Burdick <thomas.burdick@gmail.com>
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */
#ifndef KIS_OPENGL_SHADER_H_
#define KIS_OPENGL_SHADER_H_

#include "opengl/kis_opengl.h"

#include <QString>

#include "krita_export.h"

/**
 * An encapsulation of an OpenGL Shading Language shader object.
 *
 * Create a shader and load its source code. The code will be compiled
 * and if there are no errors, isValid() will return true. The shader can
 * then be attached to a KisOpenGLProgram for use.
 *
 * If the compilation failed, error messages generated by the OpenGL
 * driver can be viewed with getInfoLog().
 *
 * You cannot create a KisOpenGLShader directly, but should
 * use KisOpenGLFragmentShader or KisOpenGLVertexShader instead.
 */
class KRITAUI_EXPORT KisOpenGLShader
{
public:
    virtual ~KisOpenGLShader();

    /**
     * Load the shader source code from the QString specified by sourceCodeString.
     *
     * The source code string can be freed after loading as the shader makes a copy.
     *
     * This is a wrapper for the glShaderSource() function.
     *
     * @param sourceCodeStrings An array of pointers to the source code strings
     */
    void loadSourceCodeFromQString(QString sourceCodeString);

    /**
     * Load the shader source code from the array of strings specified by sourceCodeStrings. The number of strings
     * in the array is specified by numSourceCodeStrings. If stringLengths is NULL, each string is assumed to be
     * null terminated. If stringLengths is a value other than NULL, it points to an array containing a string length
     * for each of the corresponding elements of sourceCodeStrings. Each element in the length array may contain
     * the length of the corresponding string (the null character is not counted as part of the string length) or
     * a value less than 0 to indicate that the string is null terminated.
     *
     * The source code strings and lengths can be freed after loading as the shader makes a copy.
     *
     * This is a wrapper for the glShaderSource() function.
     *
     * @param numSourceCodeStrings The number of source code strings to load
     * @param sourceCodeStrings An array of pointers to the source code strings
     * @param stringLengths An array containing the lengths of each source code string
     */
    void loadSourceCodeFromCStrings(GLsizei numSourceCodeStrings, const GLchar **sourceCodeStrings, const GLint *stringLengths);

    /**
     * Load the shader source code from the given file, which will be searched for in the 'kis_shaders' resource
     * directory (krita/data/shaders).
     *
     * @param sourceCodeFilename The file to read the source code from
     */
    void loadSourceCodeFromFile(const QString & sourceCodeFilename);

    /**
     * Returns the handle for this shader object.
     */
    GLuint handle() const;

    /**
     * Returns true if the shader is valid and can be attached to a program. It is valid if its
     * source code was successfully loaded and compiled.
     */
    bool isValid() const;

    /**
     * Returns the information log obtained from the result of compiling the shader.
     */
    QString getInfoLog();

protected:
    KisOpenGLShader(GLenum shaderType);

    GLuint m_shader;
    bool m_valid;

private:
   KisOpenGLShader(const KisOpenGLShader&);
   KisOpenGLShader& operator=(const KisOpenGLShader&);
};

#endif // KIS_OPENGL_SHADER_H_
