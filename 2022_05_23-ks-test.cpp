#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i,j,len;

    cout<<"How many Numbers?:\t";
    cin>> len;

    float numbers[len];
    float ratioPlus[len], ratioMinus[len];
    float dPlus[len], dMinus[len];
    float dPlusMax, dMinusMax;
    float dObj,dAlpha;

    // Take Inputs
    for(i = 0; i<len; i++)
    {
        cout<<"Enter "<< i+1<< " Number :\t";
        cin>> numbers[i];
    }

    sort(numbers, numbers+len);
    cout<< "\n\nSorted Array:  "<<endl;
    for(i = 0; i<len; i++)
    {
        cout<<"  " << numbers[i];
    }

    for(j = 0; j< len; j++)
    {
        i = j+1;

        ratioPlus[j] = (float) i/len;
        ratioMinus[j] = (float) j/len;

        dPlus[j] = ratioPlus[j] - numbers[j];
        dMinus[j] = numbers[j] - ratioMinus[j];
    }

    dPlusMax = *max_element(dPlus, dPlus+len);
    dMinusMax = *max_element(dMinus, dMinus+len);

    cout << "\n\n\n D+ max :"<< dPlusMax <<endl;
    cout<< "D- max:"<< dMinusMax << endl;

    dObj = max(dPlusMax, dMinusMax);

    cout<< "dObj : " << dObj << endl;

    cout<<"Enter the tabulated value (D Alpha): ";
    cin>>dAlpha;

    if(dObj >= 0 && dObj <= dAlpha) cout << "Test is Accepted"<<endl;
    else cout << "Test is Declined"<<endl;
    return 0;
}
