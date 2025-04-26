#include<stdio.h>
int main()
{
    int row,col,nrow,count=1;
    scanf("%d",&nrow);
    for(row=nrow;row>=1;row--)
    {
        for(col=1;col<=nrow;col++)
        {
            if(col<row)
            printf(" ");
            else
            printf("%d",count);
        }
        printf("\n");
        count++;
    }
    
    return 0;
}