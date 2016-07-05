#include <stdio.h>
#include <stdlib.h>

int getLength(char string[]) {
  int i = 0;
  for (; string[i] != '\0'; i++);
  return i;
}

char* reverseString(char string[]) {
  int length = getLength(string);
  printf("%d", length);
  char reversedString[10];
  int i = length - 1;
  for(; i >= 0; i--) {
    reversedString[10 - i] += string[i];
  }

  return *reverseString;
}

int main() {
  char string[10] = "YupYupYup\0";
  char *reversedString = reverseString(string);
  printf("%s", reversedString);
  return 0;
}
