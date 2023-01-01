#include <stdio.h>

void echo() {
  char data[256];

  printf("Echo:\n");
  fflush(stdout);
  gets(data, sizeof(data));
  printf(data);
  printf("\n");
  fflush(stdout);
}

int main(int argc, char *argv[]) {
  while (1) {
    echo();
  }
}
