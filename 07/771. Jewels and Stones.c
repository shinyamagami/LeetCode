int numJewelsInStones(char * J, char * S){

    int Jl = strlen(J);
    int Sl = strlen(S);
    int count = 0;
    //printf("%lu", J);
    
    for(int i = 0; i < Jl; i++){
        for(int j = 0; j < Sl; j++){
            if(J[i] == S[j]){
                count++;
            }
        }
    }
    

    return count;
}
