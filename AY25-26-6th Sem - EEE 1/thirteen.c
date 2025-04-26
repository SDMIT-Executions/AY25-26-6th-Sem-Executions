#include<stdio.h>
int main()
{
    int row,col,nrow;
    scanf("%d",&nrow);
    for(row=5;row>=1;row--)
    {
        for(col=1;col<=row;col++)
          {
              printf("*");
          }
          printf("\n");
    }
    return 0;
}