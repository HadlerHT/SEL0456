#include <stdio.h>

double half (double x) {
	return x * 0.5;
}

double square (double x) {
	return x * x;
}

double cube (double x) {
	return x * x * x;
}


int main (void) {

	double entry[] = {2.2, 4.6, 5.5, 7.8, 23.1};

	unsigned k;
	for (k = 0; k < 5; k++) {
		printf ("The half of %.3lf equals %.3lf\n", entry[k], half(entry[k]));
		printf ("The square of %.3lf equals %.3lf\n", entry[k], square(entry[k]));
		printf ("The cube of %.3lf equals %.3lf\n\n", entry[k], cube(entry[k]));
	}
	
	return 0;
}
