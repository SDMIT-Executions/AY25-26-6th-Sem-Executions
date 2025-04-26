// a b c d 
//   1 2 
//   3 4
// e f g h 
 #include<stdio.h>
 int main()
 {
     int row,col,count=1;
     char ch ='a';
     for(row=1;row<=4;row++)
     {
         for(col=1;col<=4;col++)
         {
             if(row==1 || row==4)
             {
               printf("%c",ch);
               ch++;
             }
             else if(col==1||col==4)
             {
                 printf(" ");
             }
             else
             {
                 printf("%d",count);
                 count++;
             }
         }
         printf("\n");
     }
     
     return 0;
 }