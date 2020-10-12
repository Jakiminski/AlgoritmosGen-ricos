#include <iostream>
#include <cstring>
#include <cassert>


int log(int a,int b);

///////////////////////////////////////////////////////////////

int main(int argc, char* argv[]){

    int status=0; // Nenhum erro

    if (argc==2){

        const char* arg = argv[1]; // argumento
        
        if (!strcmp(arg,"log")){

            int a, b;
            std::cin >> a >> b;
            std::cout << log(a,b) << std::endl;

        }else{

            std::cout << "Argumento \'" << arg << "\' não existe." << std::endl;
        }

    }else if(argc>2){
        
        int i = 0;
        char* args[2];
        args[0] = argv[0]; // path do programa

        for (i=1;i<argc;i++){
            args[1] = argv[i];
            status = main(2,args);
        }
        
    }

    return status;
}

int log(int a,int b){

    assert(a>0 && b>1);
    int i=0;
    int quo = a;

    while(quo>b-1){
        //std::cout << quo << std::endl;
        quo/=b;
        i++;
    }
    //std::cout << "\nlog" << b << " " << a << " = " << i << std::endl;
    //std::cout << quo << "<=" << b-1 << std::endl;
    return i;
}