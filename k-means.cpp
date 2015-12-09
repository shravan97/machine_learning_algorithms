#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

struct point
{
	long long int x ,y;
};
//The above structure represents each point
typedef long long int ll;
main()
{



ll n,k;

cout<<"Enter the number of points and the no. of clusters : ";
cin>>n>>k;//Input total number of points and total number of clusters

point v[n];
//Also assuming that number of clusters will be less than the number of points.

ll i;//Looper
cout<<"Enter the points : ";
for(i=0;i<n;i++)//Input all the co-ordinates in pairs
{	
	point temp;
	cin>>temp.x>>temp.y;
	v[i].x=temp.x;
	v[i].y=temp.y;
}

point centroids[k];

for (i = 0; i < k; ++i)
{
	centroids[i].x=v[i].x;
	centroids[i].y=v[i].y;
}
//The above for loop randomly intializes cluster centroids to the first k input points.

ll cluster_index[k];

	//Cluster assignment
	for(i=0;i<n;i++)
	{
		double distance = (double)(sqrt(pow(centroids[0].x - v[i].x , 2) + pow(centroids[0].y - v[i].y , 2)));
		cluster_index[i]=0;
		for (ll j = 1; j < k; ++j)
		{	
			double temp_dist = (double)(sqrt(pow(centroids[j].x - v[i].x , 2) + pow(centroids[j].y - v[i].y , 2)));
			if(distance > temp_dist)
			{	
				cluster_index[i]=j;
			
			}
		}
		
	}	

return 0;

}
