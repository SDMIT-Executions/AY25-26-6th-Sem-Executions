//153 =1^3+5^3+3^3


#include<stdio.h>
#include<math.h>
int main()
{
    int num,count=0,sum=0,num2,digit;
    scanf("%d",&num);
    num2=num;
    while(num!=0)
    {
        num=num/10;
        count++;
    }
    num=num2;
    while(num!=0)
    {
        digit=num%10;
        sum=sum+pow(digit,count); 
        num=num/10;
    }
    if(num2==sum)
    {
        printf("\nAmstrong");
    }
    else{
        printf("\nNot amstrong ");
    }
    return 0;
}