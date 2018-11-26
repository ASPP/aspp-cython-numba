#include <stdio.h>
#include "runningloop_c_opt_sum.h"

int main(int argc, char **argv) {
        long int s;

        for (int i = 0; i < 10000; i++)
                s = sum(1000000);

        printf("%ld\n", s);

        return 0;
}
