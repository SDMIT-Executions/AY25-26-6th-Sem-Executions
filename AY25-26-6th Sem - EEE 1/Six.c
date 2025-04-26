#include<stdio.h>
int main()
{
    int n,i,rev=0;
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++)
    {
       rev=rev*10+arr[i];
    }
 printf("\n%d",rev);
    return 0;
}