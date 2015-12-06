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

std::vector<point> v;

long long int n,k;
cout<<"Enter the number of points and the no. of clusters : ";
cin>>n>>k;//Input total number of points and total number of clusters

//Also assuming that number of clusters will be less than the number of points.

cout<<"Enter the clusters : ";
for(ll int i=0;i<n;i++)//Input all the co-ordinates in pairs
{	
	point temp;
	cin>>temp.x>>temp.y;
	cin>>v.push_back(temp);
}

std::vector<point> centroids;

for (i = 0; i < k; ++i)
{
	centroids[i]=v[i];
}
//The above for loop randomly intializes cluster centroids to the first k input points.

return 0;

}
