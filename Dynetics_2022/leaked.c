#include <stdio.h>

void getFlag() {
  char flag[128];
  FILE *fd = fopen("flag.txt", "r");
  if (!fd) {
    printf("Need a flag.txt file");
    exit(1);
  } 
  
  // Keep this secure for now
  fgets(flag, sizeof(flag), fd);

  char password[256];
  printf("Whats the password:\n");
  fflush(stdout);
  gets(password, sizeof(password));
  printf(password);
  printf("\n");
  fflush(stdout);
}

int main(int argc, char *argv[]) {
  while (1) {
    getFlag();
  }
}
