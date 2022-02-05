#include <iostream>

using namespace std;

class Rational{
    long long num, den;
    friend istream& operator>>(istream &is, Rational &a);
    void reduce(){
        if (den<0){
            den*=-1;
            num*=-1;
        }
        long long abs_num=(num<0)?(-num):(num);
        long long s_den=den;
        while(abs_num!=0&&s_den!=0){
            if(abs_num>s_den){
                abs_num%=s_den;
            }else{s_den%=abs_num;}
        }
        long long nod=s_den+abs_num;
        den/=nod;
        num/=nod;
    }
public:
    Rational(long long a=0, long long b=1){
        num=a;
        den=b;
        reduce();
    };
    Rational operator*(Rational a){
        return Rational(num*a.num, den*a.den);
    };
    Rational operator/(Rational a){
        return Rational(num*a.den, den*a.num);
    }
    Rational operator+(Rational a){
        return Rational(num*a.den+a.num*den, den*a.den);
    }
    Rational operator-(Rational a){
        return Rational(num*a.den-a.num*den, den*a.den);
    }
    long long numerator(){
        return num;
    }
    long long denominator(){
        return den;
    }

};

ostream& operator<<(ostream &os, Rational a){
    if (a.denominator()!=1) {
        os << a.numerator() << "/" << a.denominator();
    }
    else{
        os << a.numerator();
    }
    return os;
}
istream& operator>>(istream &is, Rational &a){
    int n;
    int d;
    char skip;
    is>>n;
    if(is.peek()=='/') {
        is>>skip;
        is>>d;
        a = Rational(n, d);
    }else{
        a = Rational(n);
    }
    return is;
}
