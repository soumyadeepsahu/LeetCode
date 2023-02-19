bool isPalindrome(int x){
    if(x < 0)
        return false;
    else{
        unsigned int y = 0;
        unsigned int temp = x; 
        while(temp >= 10){
            y += temp % 10;
            y *= 10;
            temp /= 10;
        }
        y += temp;

        if(y == x)
            return true;
        else
            return false;
    }        
}