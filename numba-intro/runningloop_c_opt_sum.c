#include "runningloop_c_opt_sum.h"

long int sum(int N) {
        long int s = 0;
        for (int i=0; i <= N; i++)
                s += i;
        return s;
}
