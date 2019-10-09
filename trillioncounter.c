/*
Count to a trillion!
*/
#include <stdio.h>
#include <time.h>

#define TWO_BILLION 2000000000
int main()
{
  
  clock_t begin = clock();
  int s = 0;
  for(int j = 0; j < 250; j++){ // counting four billion 250 times 
    printf("j = %d\n", j);
    for(int i = -TWO_BILLION; i < TWO_BILLION; i++){ //counting four billion
      s = 0;
    }
  }
  
  clock_t end = clock(); 
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("Time Spent: %f\n", time_spent);
  return 0;
}
