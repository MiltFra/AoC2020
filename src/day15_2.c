#include <stdio.h>
#include <stdlib.h>

#define NUM 30000000

int *buffer;

void next(int *number) {
  register int c;
  *number = 0;
  do {
    c = getchar();
  } while (c == ',');
  if (c == EOF) {
    *number = EOF;
    return;
  }
  for (; (c > 47 && c < 58); c = getchar())
    *number = *number * 10 + c - 48;
}

int main(void) {
  buffer = malloc(NUM * sizeof(int));
  for (int i = 0; i < NUM; i++) {
    buffer[i] = -1;
  }
  int n;
  register int t, last;
  t = 0;
  next(&n);
  while (n != EOF) {
    buffer[n] = t++;
    last = n;
    next(&n);
  }
  for (; t < NUM; t++) {
    n = 0;
    if (buffer[last] >= 0) {
      n = t - 1 - buffer[last];
    }
    buffer[last] = t - 1;
    last = n;
  }
  printf("%d\n", last);
}