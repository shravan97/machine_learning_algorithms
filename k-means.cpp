#include <iostream>
#include <vector>
using namespace std;

struct pos
{
	int x ,y;
};

typedef long long ll;
main()
{

std::vector<pos> v;

long long int n,k;
cout<<"Enter the number of points and the no. of clusters : ";
cin>>n>>k;

cout<<"Enter the clusters : ";
for(ll int i=0;i<n;i++)
{	pos temp;
	cin>>temp.x>>temp.y;
	cin>>v.push_back(temp);
}

return 0;

}
