INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_REMOTECAR remotecar)

FIND_PATH(
    REMOTECAR_INCLUDE_DIRS
    NAMES remotecar/api.h
    HINTS $ENV{REMOTECAR_DIR}/include
        ${PC_REMOTECAR_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    REMOTECAR_LIBRARIES
    NAMES gnuradio-remotecar
    HINTS $ENV{REMOTECAR_DIR}/lib
        ${PC_REMOTECAR_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(REMOTECAR DEFAULT_MSG REMOTECAR_LIBRARIES REMOTECAR_INCLUDE_DIRS)
MARK_AS_ADVANCED(REMOTECAR_LIBRARIES REMOTECAR_INCLUDE_DIRS)

