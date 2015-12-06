#include <iostream>
#include <vector>
using namespace std;

struct point
{
	int x ,y;
};
//The above structure represents each point
typedef long long ll;
main()
{

std::vector<pos> v;

long long int n,k;
cout<<"Enter the number of points and the no. of clusters : ";
cin>>n>>k;//Input total number of points and total number of clusters

cout<<"Enter the clusters : ";
for(ll int i=0;i<n;i++)//Input all the co-ordinates in pairs
{	point temp;
	cin>>temp.x>>temp.y;
	cin>>v.push_back(temp);
}


return 0;

}
