// 2  4  6  8
// 1  3  5  
// 10 12 14 16
// 9  11 13 
// 18 20 22 24
// 2  4  6  8
// 1  3  5  
// 10 12 14 16
// 9  11 13 
// 18 20 22 24
#include<stdio.h>
int main()
{
    int row,col,ncol,evencount=2,oddcount=1,nrow;
    scanf("%d",nrow);
    for(row=1;row<=nrow;row++)
    {
        if(row%2==0)
        {
        ncol=nrow-2;
        }
        else
        {
        ncol=nrow-1;
        }
        for(col=1;col<=ncol;col++)
        {
            if(row%2!=0)
            {
            printf("%d ",evencount);
            evencount+=2;
            }
            else{
                printf("%d ",oddcount);
            oddcount+=2;
            }
        }
        printf("\n");
    }
    
    return 0;
}