// 5
// 12340
// 23401
// 34012
// 40123
// 01234

#include<stdio.h>
int main()
{
    int row,col,count=1,nrow;
    scanf("%d",&nrow);
    for(row=1;row<=nrow;row++)
    {
        count=row;
        for(col=1;col<=nrow;col++)
        {
            if(count==nrow)
              count=0;
            printf("%d",count);
            count++;
        }
        printf("\n");
    }
    
    
    return 0;
}








