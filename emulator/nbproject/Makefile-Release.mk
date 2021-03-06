#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Environment
MKDIR=mkdir
CP=cp
GREP=grep
NM=nm
CCADMIN=CCadmin
RANLIB=ranlib
CC=gcc
CCC=g++
CXX=g++
FC=gfortran
AS=as

# Macros
CND_PLATFORM=GNU-Linux
CND_DLIB_EXT=so
CND_CONF=Release
CND_DISTDIR=dist
CND_BUILDDIR=build

# Include project Makefile
include Makefile

# Object Directory
OBJECTDIR=${CND_BUILDDIR}/${CND_CONF}/${CND_PLATFORM}

# Object Files
OBJECTFILES= \
	${OBJECTDIR}/framework/debugger.o \
	${OBJECTDIR}/framework/gfx.o \
	${OBJECTDIR}/framework/main.o \
	${OBJECTDIR}/hardware.o \
	${OBJECTDIR}/sys_debug_1802.o \
	${OBJECTDIR}/sys_processor.o


# C Compiler Flags
CFLAGS=

# CC Compiler Flags
CCFLAGS=
CXXFLAGS=

# Fortran Compiler Flags
FFLAGS=

# Assembler Flags
ASFLAGS=

# Link Libraries and Options
LDLIBSOPTIONS=/usr/lib/libSDL2.so

# Build Targets
.build-conf: ${BUILD_SUBPROJECTS}
	"${MAKE}"  -f nbproject/Makefile-${CND_CONF}.mk ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/emulator

${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/emulator: /usr/lib/libSDL2.so

${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/emulator: ${OBJECTFILES}
	${MKDIR} -p ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}
	${LINK.cc} -o ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/emulator ${OBJECTFILES} ${LDLIBSOPTIONS}

${OBJECTDIR}/framework/debugger.o: framework/debugger.cpp
	${MKDIR} -p ${OBJECTDIR}/framework
	${RM} "$@.d"
	$(COMPILE.cc) -O2 -DINCLUDE_DEBUGGING_SUPPORT -I/usr/include/SDL2 -I. -I./framework -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/framework/debugger.o framework/debugger.cpp

${OBJECTDIR}/framework/gfx.o: framework/gfx.cpp
	${MKDIR} -p ${OBJECTDIR}/framework
	${RM} "$@.d"
	$(COMPILE.cc) -O2 -DINCLUDE_DEBUGGING_SUPPORT -I/usr/include/SDL2 -I. -I./framework -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/framework/gfx.o framework/gfx.cpp

${OBJECTDIR}/framework/main.o: framework/main.cpp
	${MKDIR} -p ${OBJECTDIR}/framework
	${RM} "$@.d"
	$(COMPILE.cc) -O2 -DINCLUDE_DEBUGGING_SUPPORT -I/usr/include/SDL2 -I. -I./framework -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/framework/main.o framework/main.cpp

${OBJECTDIR}/hardware.o: hardware.cpp
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -O2 -DINCLUDE_DEBUGGING_SUPPORT -I/usr/include/SDL2 -I. -I./framework -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/hardware.o hardware.cpp

${OBJECTDIR}/sys_debug_1802.o: sys_debug_1802.cpp
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -O2 -DINCLUDE_DEBUGGING_SUPPORT -I/usr/include/SDL2 -I. -I./framework -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/sys_debug_1802.o sys_debug_1802.cpp

${OBJECTDIR}/sys_processor.o: sys_processor.cpp
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -O2 -DINCLUDE_DEBUGGING_SUPPORT -I/usr/include/SDL2 -I. -I./framework -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/sys_processor.o sys_processor.cpp

# Subprojects
.build-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r ${CND_BUILDDIR}/${CND_CONF}
	${RM} -r ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libSDL2.so
	${RM} ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/emulator

# Subprojects
.clean-subprojects:

# Enable dependency checking
.dep.inc: .depcheck-impl

include .dep.inc
