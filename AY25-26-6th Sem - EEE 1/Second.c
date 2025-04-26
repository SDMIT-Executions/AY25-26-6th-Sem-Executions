#include<stdio.h>
int main()
{
    int n,sum;
    scanf("%d",&n);
    int arr[n];
    for(int i =0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    sum=0;
    for(int i =0;i<n;i++)
    {
        sum= sum+arr[i];
    }
    printf("\n%d",sum);
    return 0;
}