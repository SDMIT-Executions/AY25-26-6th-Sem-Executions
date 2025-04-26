#include<stdio.h>
int main()
{
    int n,i;
    scanf("%d",&n);
    int arr[n],temp;
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n-1;i++)
    {
       for(int j =i+1;j<n;j++)
       {
           if(arr[i]>arr[j])
           {
               temp=arr[i];
               arr[i]=arr[j];
               arr[j]=temp;
           }
       }
    }
    for(i=0;i<n;i++)
    {
        printf("\t%d",arr[i]);
    }
    return 0;
}