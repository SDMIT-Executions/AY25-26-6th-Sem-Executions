#include<stdio.h>
int main()
{
    int n,i,max,min,minpos=1,maxpos=1;
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    max=arr[0];
    min=arr[0];
    for(i=0;i<n;i++)
    {
        if(max<arr[i])
        {
            max=arr[i];
            maxpos=i+1;
        }
        if(min>arr[i])
        {
            min=arr[i];
            minpos=i+1;
        }
    }
    printf("\nmax:%d pos:%d",max,maxpos);
    printf("\nmin:%d pos:%d",min,minpos);
    return 0;
}