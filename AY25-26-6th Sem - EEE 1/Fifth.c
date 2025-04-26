#include<stdio.h>
int main()
{
    int n,i,ecount=0,ocount=0;
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++)
    {
        if(arr[i]%2==0)
        ecount++;
        else
        ocount++;
    }
    if(ecount>ocount)
    printf("\nstrong array")
    else
    printf("\nNot a Strong array");
    return 0;
}