dnl Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
AC_INIT([calc], [0.0.1], [help@codio.com])

AC_CONFIG_AUX_DIR([build-aux])
AC_CONFIG_MACRO_DIR([m4])
AC_CANONICAL_SYSTEM
AM_INIT_AUTOMAKE([foreign -Wall -Werror])


AC_PROG_CC
dnl this allows us specify individual liking flags for each target
AM_PROG_CC_C_O 
AM_PROG_AR
dnl Initialize Libtool
LT_INIT

PKG_CHECK_MODULES([CHECK], [check])

dnl Check if Libtool is present
dnl Libtool is used for building share libraries 
AC_PROG_LIBTOOL


AC_CONFIG_FILES(Makefile 
                src/Makefile
                tests/Makefile
                )

AC_OUTPUT

