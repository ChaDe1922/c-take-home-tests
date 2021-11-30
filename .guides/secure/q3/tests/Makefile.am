## Process this file with automake to produce Makefile.in

TESTS = check_f
check_PROGRAMS = check_f
check_f_SOURCES = check_f.c $(top_builddir)/src/q3.h
check_f_CFLAGS = @CHECK_CFLAGS@
check_f_LDADD = $(top_builddir)/src/libq1.la @CHECK_LIBS@