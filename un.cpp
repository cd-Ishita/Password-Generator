#include<iostream>
using namespace std;
int main() {
    int d, sum, i, sum1=0, final;
    cin>>d>>sum;
    int min[d];
    int max[d];
    for(i=0;i<d;i++){
        cin>>min[i]>>max[i];
        sum1 = sum1 + max[i];
    }
    
    // for(i=0;i<d;i++){
    //     sum1 = sum1+max[i];
    // }   
    int diff[d];
    if(sum1 < sum){
        cout<<"NO";
    }
    
    
    else{
        cout<<"YES"<<endl;
        final = sum;
        for(i=0;i<d;i++){
            final = final - min[i];
            diff[i] = max[i] - min[i];
        }
        
        for(i=0;i<d;i++){
            if(diff[i]<=final){
                final = final - diff[i];
                cout<<max[i]<<" ";
            }
            else if(final < diff[i] && final != 0){
                cout<<min[i]+final<<" ";
            }
            
            else if(final == 0)
            {
                cout<<min[i]<<" ";
            }
            
        }
    }
}