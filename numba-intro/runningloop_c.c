#include <stdio.h>

static long int sum(int N) {
        long int s = 0;
        for (int i=0; i <= N; i++)
                s += i;
        return s;
}

int main(int argc, char **argv) {
        long int s;

        for (int i = 0; i < 10000; i++)
                s = sum(1000000);

        printf("%ld\n", s);

        return 0;
}
