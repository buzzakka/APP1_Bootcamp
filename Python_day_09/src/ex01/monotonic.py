import ctypes
# import time

__all__ = ('monotonic',)

libc = ctypes.CDLL('/usr/lib/libc.dylib', use_errno=True)


class mach_timebase_info_data_t(ctypes.Structure):
    """System timebase info. Defined in <mach/mach_time.h>."""
    _fields_ = (('numer', ctypes.c_uint32),
                ('denom', ctypes.c_uint32))


mach_absolute_time = libc.mach_absolute_time
mach_absolute_time.restype = ctypes.c_uint64
timebase = mach_timebase_info_data_t()
libc.mach_timebase_info(ctypes.byref(timebase))

NANOSECONDS_IN_SECOND = 1.0e9


def monotonic():
    nanoseconds = mach_absolute_time() * timebase.numer / timebase.denom
    return nanoseconds / NANOSECONDS_IN_SECOND


# for tests you need also uncomment import time
# if __name__ == "__main__":
#     print(monotonic())
    # print(time.monotonic())
