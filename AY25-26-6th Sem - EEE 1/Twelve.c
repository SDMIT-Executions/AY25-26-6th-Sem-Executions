#include<stdio.h>
int main()
{
    int row,col,nrow;
    char ch='a';
    scanf("%d",&nrow);
    for(row=nrow;row>=1;row--)
    {
        for(col=1;col<=nrow;col++)
        {
            if(col<row)
            printf(" ");
            else
            {
            printf("%c",ch);
            ch++;
            }
        }
        printf("\n");
      
    }
    
    return 0;
}