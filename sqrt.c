#include <stdio.h>
#include <math.h>
int main()
{
float x,y,result;
printf("please choose a number to start with: ");
scanf("%f",&x);
printf("please enter the order of the root: ");
scanf("%f",&y);
for (int i = x ; i < x + 10 ; i++)
{
result=pow(i,1/y);
printf("square root of %d is : %0.2f\n",i,result);
}

return 0;
}
