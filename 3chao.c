#include <stdio.h>
void hello(char* s);
void chao(char* s);
void bonjuor(char* s);
void main(){
	hello("ABC");
	chao("abc");
	bonjuor("abc");
}

void hello(char* s){
	printf("hello %s\n", s);
}
void chao(char* s){
	printf("chao %s\n", s);
}
void bonjuor(char* s){
	printf("hello %s\n", s);
}
