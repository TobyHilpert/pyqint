# distutils: language = c++

from libcpp.vector cimport vector

# Integrals
cdef extern from "integrals.cpp":
    pass

# contracted and primitive Gaussians
cdef extern from "cgf.cpp":
    pass

# Gamma and incomplete Gamma function
cdef extern from "gamma.cpp":
    pass

# Declare the class with cdef
cdef extern from "cgf.h":
    cdef cppclass GTO:
        GTO() except +
        GTO(double, double, double, double, double, int, int, int) except +
        double get_amp(double, double, double) except +

    cdef cppclass CGF:
        CGF() except +
        CGF(double, double, double) except +
        void add_gto(double, double, int, int, int) except +
        double get_amp(double, double, double) except +

# Declare the class with cdef
cdef extern from "integrals.h":
    cdef cppclass Integrator:
        Integrator() except +
        double overlap(GTO, GTO) except +
        double overlap(CGF, CGF) except +

        double kinetic(GTO, GTO) except +
        double kinetic(CGF, CGF) except +

        double nuclear(GTO, GTO, double, double, double) except +
        double nuclear(CGF, CGF, double, double, double, int) except +

        double repulsion(GTO, GTO, GTO, GTO) except +
        double repulsion(CGF, CGF, CGF, CGF) except +

        int teindex(int, int, int, int) except +

        const char* get_compile_date() except+
        const char* get_compile_time() except+

        vector[double] evaluate_cgfs(vector[CGF], vector[int], vector[double], vector[double], vector[double]) except+
