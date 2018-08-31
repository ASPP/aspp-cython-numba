#include <stdio.h>
#include <math.h>

double f(double x) {
        double y = (x*x*x - 3)*x;
        return y;
}

double integrate_f9(double a, double b, int n) {
        double dx = (b - a) / n;
        double dx2 = dx / 2;
        double s = f(a) * dx2;
        for (int i = 1; i < n; i++)
                s += f(a + i*dx) * dx;
        s += f(b) * dx2;
        return s;
}

int main(int argc, char **argv) {
        double x;
        
        for (int i = 0; i < 1000; i++)
                x = integrate_f9(-100, +100, 100000);

        printf("x=%f\n", x);
        return 0;
}
