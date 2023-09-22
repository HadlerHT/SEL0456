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

	double entry;

	printf ("Type in a number: ");
	scanf ("%lf", &entry);
	
	printf ("The half of %.3lf equals %.3lf\n", entry, half(entry));
	printf ("The square of %.3lf equals %.3lf\n", entry, square(entry));
	printf ("The cube of %.3lf equals %.3lf\n", entry, cube(entry));
		
	return 0;
}
