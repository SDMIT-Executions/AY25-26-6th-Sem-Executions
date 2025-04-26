#include<stdio.h>
int main()
{
    int n,i,target;
    scanf("%d",&n);
    int arr[n],temp;
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    scanf("%d",&target);
    for(i=0;i<n-1;i++)
    {
        for(int j = i+1;j<n;j++)
        {
            if(arr[i]+arr[j]==target)
            printf("\n %d  %d",arr[i],arr[j]);
        }
    }
    return 0;
}