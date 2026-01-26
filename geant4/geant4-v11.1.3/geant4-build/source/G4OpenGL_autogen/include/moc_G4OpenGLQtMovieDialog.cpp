/****************************************************************************
** Meta object code from reading C++ file 'G4OpenGLQtMovieDialog.hh'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.12.8)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "G4OpenGLQtMovieDialog.hh"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'G4OpenGLQtMovieDialog.hh' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.12.8. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_G4OpenGLQtMovieDialog_t {
    QByteArrayData data[12];
    char stringdata0[227];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_G4OpenGLQtMovieDialog_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_G4OpenGLQtMovieDialog_t qt_meta_stringdata_G4OpenGLQtMovieDialog = {
    {
QT_MOC_LITERAL(0, 0, 21), // "G4OpenGLQtMovieDialog"
QT_MOC_LITERAL(1, 22, 15), // "stopFinishClose"
QT_MOC_LITERAL(2, 38, 0), // ""
QT_MOC_LITERAL(3, 39, 4), // "save"
QT_MOC_LITERAL(4, 44, 24), // "checkEncoderSwParameters"
QT_MOC_LITERAL(5, 69, 27), // "checkSaveFileNameParameters"
QT_MOC_LITERAL(6, 97, 25), // "checkTempFolderParameters"
QT_MOC_LITERAL(7, 123, 23), // "selectEncoderPathAction"
QT_MOC_LITERAL(8, 147, 20), // "selectTempPathAction"
QT_MOC_LITERAL(9, 168, 24), // "selectSaveFileNameAction"
QT_MOC_LITERAL(10, 193, 14), // "resetRecording"
QT_MOC_LITERAL(11, 208, 18) // "enabledApplyButton"

    },
    "G4OpenGLQtMovieDialog\0stopFinishClose\0"
    "\0save\0checkEncoderSwParameters\0"
    "checkSaveFileNameParameters\0"
    "checkTempFolderParameters\0"
    "selectEncoderPathAction\0selectTempPathAction\0"
    "selectSaveFileNameAction\0resetRecording\0"
    "enabledApplyButton"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_G4OpenGLQtMovieDialog[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      10,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   64,    2, 0x0a /* Public */,
       3,    0,   65,    2, 0x0a /* Public */,
       4,    0,   66,    2, 0x0a /* Public */,
       5,    0,   67,    2, 0x0a /* Public */,
       6,    0,   68,    2, 0x0a /* Public */,
       7,    0,   69,    2, 0x08 /* Private */,
       8,    0,   70,    2, 0x08 /* Private */,
       9,    0,   71,    2, 0x08 /* Private */,
      10,    0,   72,    2, 0x08 /* Private */,
      11,    0,   73,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Bool,
    QMetaType::Bool,
    QMetaType::Bool,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void G4OpenGLQtMovieDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<G4OpenGLQtMovieDialog *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->stopFinishClose(); break;
        case 1: _t->save(); break;
        case 2: { bool _r = _t->checkEncoderSwParameters();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = std::move(_r); }  break;
        case 3: { bool _r = _t->checkSaveFileNameParameters();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = std::move(_r); }  break;
        case 4: { bool _r = _t->checkTempFolderParameters();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = std::move(_r); }  break;
        case 5: _t->selectEncoderPathAction(); break;
        case 6: _t->selectTempPathAction(); break;
        case 7: _t->selectSaveFileNameAction(); break;
        case 8: _t->resetRecording(); break;
        case 9: _t->enabledApplyButton(); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject G4OpenGLQtMovieDialog::staticMetaObject = { {
    &QDialog::staticMetaObject,
    qt_meta_stringdata_G4OpenGLQtMovieDialog.data,
    qt_meta_data_G4OpenGLQtMovieDialog,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *G4OpenGLQtMovieDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *G4OpenGLQtMovieDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_G4OpenGLQtMovieDialog.stringdata0))
        return static_cast<void*>(this);
    return QDialog::qt_metacast(_clname);
}

int G4OpenGLQtMovieDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 10)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 10;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
